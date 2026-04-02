import pytest
from courses.views import _extraire_youtube_id, _generer_video_html


def test_extraire_youtube_id_is_safe():
    """
    Teste: L'extraction d'ID YouTube ignore les tentatives d'injection XSS dans l'URL
    Raison: Un attaquant pourrait injecter du JavaScript via une URL YouTube malveillante
    Features: extraction YouTube, sécurité XSS
    Criticité: haute
    """
    malicious_urls = [
        # XSS collé après un ID valide
        'https://www.youtube.com/watch?v=dQw4w9WgXcQ"<script>alert(1)</script>',
        # Paramètres supplémentaires avec injection
        'https://youtu.be/dQw4w9WgXcQ?t=10" onerror="alert(1)',
        # Tentative d'évasion complète
        'javascript:alert(1)//https://youtube.com/watch?v=dQw4w9WgXcQ',
    ]

    for url in malicious_urls:
        extracted_id = _extraire_youtube_id(url)
        # S'il trouve un ID, il DOIT faire exactement 11 caractères et ne contenir aucun caractère dangereux
        if extracted_id:
            assert len(extracted_id) == 11
            assert "<" not in extracted_id
            assert '"' not in extracted_id
            assert extracted_id == "dQw4w9WgXcQ"


def test_generer_video_html_escapes_title():
    """
    Teste: Le titre de la leçon est échappé HTML pour empêcher l'injection XSS via l'attribut title
    Raison: Un titre malveillant pourrait fermer l'attribut et injecter un événement JavaScript
    Features: rendu vidéo, sécurité XSS, échappement HTML
    Criticité: haute
    """
    class MockLecon:
        # Titre malveillant cherchant à fermer l'attribut title et injecter un événement
        titre = 'Vidéo de test" onload="alert(\'XSS\')"'
        video_fichier = None

    lecon = MockLecon()
    youtube_id = "dQw4w9WgXcQ"

    html = _generer_video_html(lecon, youtube_id)

    # Le guillemet doit être échappé (en &quot; ou similaire par Django)
    assert 'title="Vidéo de test&quot; onload=&quot;alert(&#x27;XSS&#x27;)&quot;"' in html

    # La chaîne brute dangereuse ne doit pas se trouver dans le HTML final
    assert 'Vidéo de test" onload="alert' not in html