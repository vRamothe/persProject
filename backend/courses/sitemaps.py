from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Matiere, Lecon


class CatalogueSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Matiere.objects.all()

    def location(self, obj):
        return reverse("catalogue_matiere", kwargs={"matiere_slug": obj.slug})


class LeconPubliqueSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Lecon.objects.filter(gratuit=True).select_related("chapitre__matiere")

    def location(self, obj):
        lecon = obj
        chapitre = lecon.chapitre
        return reverse(
            "lecon_publique",
            kwargs={
                "matiere_slug": chapitre.matiere.slug,
                "niveau": chapitre.niveau,
                "chapitre_slug": chapitre.slug,
                "lecon_slug": lecon.slug,
            },
        )

    def lastmod(self, obj):
        return obj.updated_at
