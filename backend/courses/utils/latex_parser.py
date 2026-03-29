import logging
import os
import re
import subprocess
import tempfile
from html import escape as html_escape

import bleach
import markdown

logger = logging.getLogger(__name__)


def proteger_latex(contenu):
    """Protège les blocs LaTeX ($$...$$ et $...$) du traitement Markdown."""
    placeholders = {}
    counter = 0

    def _remplacer(match):
        nonlocal counter
        key = f"LATEXPLACEHOLDER{counter}"
        placeholders[key] = match.group(0)
        counter += 1
        return key

    contenu = re.sub(r'\$\$.+?\$\$', _remplacer, contenu, flags=re.DOTALL)
    contenu = re.sub(r'\$(?!\$).+?\$', _remplacer, contenu, flags=re.DOTALL)
    return contenu, placeholders


def restaurer_latex(html, placeholders):
    """Réinsère les blocs LaTeX originaux dans le HTML rendu."""
    for key, latex in placeholders.items():
        html = html.replace(key, latex)
    return html


def nettoyer_svg(svg_content, prefix):
    """Nettoie le SVG produit par dvisvgm pour l'intégration inline."""
    svg_content = re.sub(r'<\?xml[^?]*\?>\s*', '', svg_content)
    svg_content = re.sub(r'<!--[\s\S]*?-->\s*', '', svg_content)
    svg_content = re.sub(r"""\bid=(['"])([^'"]+)\1""", rf'id=\1{prefix}-\2\1', svg_content)
    svg_content = re.sub(r"""xlink:href=(['"])#([^'"]+)\1""", rf'xlink:href=\1#{prefix}-\2\1', svg_content)
    svg_content = re.sub(r"""(?<!xlink:)href=(['"])#([^'"]+)\1""", rf'href=\1#{prefix}-\2\1', svg_content)
    svg_content = re.sub(r'url\(#([^)]+)\)', rf'url(#{prefix}-\1)', svg_content)
    return svg_content.strip()


def compiler_equations_latex(equations):
    """Compile toutes les équations en un seul appel LaTeX + dvisvgm."""
    if not equations:
        return {}

    tex_parts = [
        r'\documentclass[11pt]{article}', r'\usepackage{amsmath}',
        r'\usepackage{amssymb}', r'\usepackage{amsfonts}',
        r'\pagestyle{empty}', r'\begin{document}',
    ]
    for i, (key, inner, is_display) in enumerate(equations):
        if i > 0: tex_parts.append(r'\newpage')
        tex_parts.append(f'\\[{inner}\\]' if is_display else f'${inner}$')
    tex_parts.append(r'\end{document}')
    tex_content = '\n'.join(tex_parts)

    svgs = {}
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            tex_path = os.path.join(tmpdir, 'eq.tex')
            with open(tex_path, 'w') as f: f.write(tex_content)

            subprocess.run(
                ['latex', '-interaction=nonstopmode', '-output-directory', tmpdir, tex_path],
                capture_output=True, timeout=30,
            )
            dvi_path = os.path.join(tmpdir, 'eq.dvi')
            if not os.path.exists(dvi_path):
                logger.warning("LaTeX : pas de DVI produit")
                return {}

            n = len(equations)
            subprocess.run(
                ['dvisvgm', '--no-fonts', '--exact-bbox', f'--page=1-{n}',
                 '-o', os.path.join(tmpdir, 'eq-%p.svg'), dvi_path],
                capture_output=True, timeout=30,
            )

            for fname in os.listdir(tmpdir):
                m = re.match(r'eq-0*(\d+)\.svg$', fname)
                if m:
                    page = int(m.group(1))
                    idx = page - 1
                    if 0 <= idx < n:
                        with open(os.path.join(tmpdir, fname), 'r') as f:
                            svg = f.read()
                        svgs[idx] = nettoyer_svg(svg, f'eq{idx}')
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError) as e:
        logger.warning("Pipeline LaTeX→SVG échoué : %s", e)

    return svgs


def restaurer_latex_svg(html, placeholders):
    """Convertit les blocs LaTeX en SVG via le moteur LaTeX + dvisvgm."""
    if not placeholders:
        return html

    equations = []
    for key in sorted(placeholders.keys(), key=lambda k: int(re.search(r'\d+', k).group())):
        raw = placeholders[key]
        is_display = raw.startswith("$$") and raw.endswith("$$")
        inner = raw[2:-2].strip() if is_display else raw[1:-1].strip()
        equations.append((key, inner, is_display))

    svgs = compiler_equations_latex(equations)

    for i, (key, inner, is_display) in enumerate(equations):
        svg = svgs.get(i)
        if svg:
            if is_display:
                html = html.replace(key, f'<div class="math-block">{svg}</div>')
            else:
                html = html.replace(key, f'<span class="math-inline">{svg}</span>')
        else:
            html = html.replace(key, html_escape(placeholders[key]))

    return html


def render_markdown_to_html(contenu_md, latex_to_svg=False):
    """
    Rend le contenu Markdown en HTML, en traitant les blocs LaTeX.
    """
    if not contenu_md:
        return ""

    contenu_protege, placeholders_latex = proteger_latex(contenu_md)
    md = markdown.Markdown(extensions=["extra", "tables", "toc", "nl2br"])
    contenu_html = md.convert(contenu_protege)

    # Nettoyage XSS avec Bleach
    allowed_tags = [
        "h1", "h2", "h3", "h4", "h5", "h6", "p", "a", "ul", "ol", "li",
        "strong", "em", "code", "pre", "blockquote", "img", "table", 
        "thead", "tbody", "tr", "th", "td", "br", "hr", "div", "span"
    ]
    allowed_attrs = {
        "*": ["class", "id"],
        "a": ["href", "title", "target"],
        "img": ["src", "alt", "title"],
    }
    contenu_html = bleach.clean(contenu_html, tags=allowed_tags, attributes=allowed_attrs)

    if latex_to_svg:
        contenu_html = restaurer_latex_svg(contenu_html, placeholders_latex)
    else:
        contenu_html = restaurer_latex(contenu_html, placeholders_latex)

    return contenu_html
