from django.http import JsonResponse
from django.shortcuts import render


def custom_404(request, exception):
    return render(request, "404.html", status=404)


def custom_500(request):
    return render(request, "500.html", status=500)


def health_view(request):
    """Endpoint de santé pour les moniteurs de disponibilité (no DB query)."""
    return JsonResponse({"status": "ok"})
