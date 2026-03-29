import pytest
from unittest.mock import patch

from courses.utils.latex_parser import (
    proteger_latex,
    restaurer_latex,
    nettoyer_svg,
    compiler_equations_latex,
    restaurer_latex_svg,
    render_markdown_to_html,
)

def test_proteger_latex():
    contenu = "Texte normal avec $$a^2 + b^2 = c^2$$ (display) et $x=1$ (inline)."
    protege, placeholders = proteger_latex(contenu)
    assert "$$" not in protege
    assert "$" not in protege
    assert len(placeholders) == 2

def test_restaurer_latex():
    html = "<p>Texte LATEXPLACEHOLDER0</p>"
    placeholders = {"LATEXPLACEHOLDER0": "$x=1$"}
    assert restaurer_latex(html, placeholders) == "<p>Texte $x=1$</p>"

def test_nettoyer_svg():
    raw_svg = '<?xml version="1.0"?>\n<!-- gen -->\n<svg id="page1"><use xlink:href="#g1"/><use href="#g2"/><clipPath id="c1"/><g clip-path="url(#c1)"/></svg>'
    cleaned = nettoyer_svg(raw_svg, "eq0")
    assert "<?xml" not in cleaned
    assert 'id="eq0-page1"' in cleaned
    assert 'xlink:href="#eq0-g1"' in cleaned
    assert 'href="#eq0-g2"' in cleaned
    assert 'id="eq0-c1"' in cleaned
    assert 'url(#eq0-c1)' in cleaned

def test_compiler_equations_latex_vide():
    assert compiler_equations_latex([]) == {}

@patch("courses.utils.latex_parser.compiler_equations_latex")
def test_restaurer_latex_svg(mock_compiler):
    mock_compiler.return_value = {0: "<svg>inline</svg>", 1: "<svg>display</svg>"}
    html = "<p>LATEXPLACEHOLDER0 LATEXPLACEHOLDER1</p>"
    placeholders = {"LATEXPLACEHOLDER0": "$x=1$", "LATEXPLACEHOLDER1": "$$y=2$$"}
    result = restaurer_latex_svg(html, placeholders)
    assert '<span class="math-inline"><svg>inline</svg></span>' in result
    assert '<div class="math-block"><svg>display</svg></div>' in result

def test_render_markdown_to_html_without_svg():
    md = "# Titre\n\n$x=1$"
    html = render_markdown_to_html(md, latex_to_svg=False)
    assert '<h1 id="titre">Titre</h1>' in html
    assert "$x=1$" in html

@patch("courses.utils.latex_parser.restaurer_latex_svg")
def test_render_markdown_to_html_with_svg(mock_restaurer_svg):
    mock_restaurer_svg.return_value = "<p>SVG</p>"
    assert render_markdown_to_html("Test $x$", latex_to_svg=True) == "<p>SVG</p>"
    mock_restaurer_svg.assert_called_once()

@patch("courses.utils.latex_parser.compiler_equations_latex")
def test_restaurer_latex_svg_fallback_on_failure(mock_compiler):
    mock_compiler.return_value = {}
    html = "<p>LATEXPLACEHOLDER0</p>"
    placeholders = {"LATEXPLACEHOLDER0": "$x < 2 & y > 1$"}
    result = restaurer_latex_svg(html, placeholders)
    assert "$x &lt; 2 &amp; y &gt; 1$" in result
