def tronquer_contenu_markdown(contenu: str, max_mots: int = 2000) -> tuple[str, bool]:
    """
    Tronque le contenu Markdown à max_mots mots.
    Retourne (contenu_tronque, a_ete_tronque).
    Coupe au dernier \\n\\n avant le mot max_mots pour préserver la structure Markdown.
    """
    mots = contenu.split()
    if len(mots) <= max_mots:
        return (contenu, False)

    # Reconstituer le texte jusqu'au mot max_mots
    texte_limite = " ".join(mots[:max_mots])

    # Chercher le dernier \n\n dans le texte limité (dans le contenu original)
    # On cherche dans le contenu original jusqu'à la position du dernier caractère de texte_limite
    position_limite = len(texte_limite)
    sous_contenu = contenu[:position_limite]

    dernier_saut = sous_contenu.rfind("\n\n")
    if dernier_saut > 0:
        return (contenu[:dernier_saut], True)

    # Pas de \n\n trouvé → couper au mot max_mots
    return (texte_limite, True)
