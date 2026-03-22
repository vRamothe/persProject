from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

def _home_view(request):
    if request.user.is_authenticated:
        return redirect("tableau_de_bord")
    from courses.views import accueil_view
    return accueil_view(request)

urlpatterns = [
    path("", _home_view, name="home"),
    path("django-admin/", admin.site.urls),
    path("", include("users.urls")),
    path("cours/", include("courses.urls")),
    path("progression/", include("progress.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "ScienceLycée — Administration"
admin.site.site_title = "ScienceLycée"
admin.site.index_title = "Panneau d'administration"

handler404 = "config.views.custom_404"
handler500 = "config.views.custom_500"
