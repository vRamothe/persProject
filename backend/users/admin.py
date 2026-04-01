from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Abonnement


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ["email", "prenom", "nom", "role", "niveau", "is_active", "date_joined"]
    list_filter = ["role", "niveau", "is_active"]
    search_fields = ["email", "prenom", "nom"]
    ordering = ["nom", "prenom"]

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Informations personnelles", {"fields": ("prenom", "nom", "role", "niveau")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "prenom", "nom", "role", "niveau", "password1", "password2"),
        }),
    )

    readonly_fields = ["date_joined"]


@admin.register(Abonnement)
class AbonnementAdmin(admin.ModelAdmin):
    list_display = ("user", "plan", "statut", "date_debut", "date_fin")
    list_filter = ("plan", "statut")
    search_fields = ("user__email", "stripe_customer_id", "stripe_subscription_id")
    readonly_fields = ("stripe_customer_id", "stripe_subscription_id", "created_at", "updated_at")
