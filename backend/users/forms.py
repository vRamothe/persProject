from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from .models import CustomUser, NiveauChoices


class ConnexionForm(AuthenticationForm):
    username = forms.EmailField(
        label="Adresse email",
        widget=forms.EmailInput(attrs={
            "class": "w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent",
            "placeholder": "votre@email.fr",
            "autocomplete": "email",
        }),
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent",
            "placeholder": "••••••••",
            "autocomplete": "current-password",
        }),
    )

    error_messages = {
        "invalid_login": "Adresse email ou mot de passe incorrect.",
        "inactive": "Ce compte a été désactivé.",
    }


class InscriptionForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent",
            "placeholder": "••••••••",
        }),
        help_text="Au moins 8 caractères avec une majuscule et un chiffre.",
    )
    password2 = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent",
            "placeholder": "••••••••",
        }),
    )
    niveau = forms.ChoiceField(
        label="Votre classe",
        choices=[("", "--- Choisir votre classe ---")] + list(NiveauChoices.choices),
        widget=forms.Select(attrs={
            "class": "w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent bg-white",
        }),
    )

    class Meta:
        model = CustomUser
        fields = ["prenom", "nom", "email", "niveau"]
        widgets = {
            "prenom": forms.TextInput(attrs={
                "class": "w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent",
                "placeholder": "Marie",
                "autocomplete": "given-name",
            }),
            "nom": forms.TextInput(attrs={
                "class": "w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent",
                "placeholder": "Dupont",
                "autocomplete": "family-name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent",
                "placeholder": "marie.dupont@lycee.fr",
                "autocomplete": "email",
            }),
        }
        labels = {
            "prenom": "Prénom",
            "nom": "Nom de famille",
            "email": "Adresse email",
        }

    def clean_password1(self):
        pwd = self.cleaned_data.get("password1", "")
        if len(pwd) < 8:
            raise ValidationError("Le mot de passe doit contenir au moins 8 caractères.")
        if not any(c.isupper() for c in pwd):
            raise ValidationError("Le mot de passe doit contenir au moins une lettre majuscule.")
        if not any(c.isdigit() for c in pwd):
            raise ValidationError("Le mot de passe doit contenir au moins un chiffre.")
        return pwd

    def clean_password2(self):
        pwd1 = self.cleaned_data.get("password1")
        pwd2 = self.cleaned_data.get("password2")
        if pwd1 and pwd2 and pwd1 != pwd2:
            raise ValidationError("Les deux mots de passe ne correspondent pas.")
        return pwd2

    def clean_email(self):
        email = self.cleaned_data.get("email", "").lower()
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Un compte avec cette adresse email existe déjà.")
        return email

    def clean_niveau(self):
        niveau = self.cleaned_data.get("niveau")
        if not niveau:
            raise ValidationError("Veuillez sélectionner votre classe.")
        return niveau

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"].lower()
        user.set_password(self.cleaned_data["password1"])
        user.role = "eleve"
        if commit:
            user.save()
        return user


class ProfilForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["prenom", "nom", "email", "niveau"]
        widgets = {
            "prenom": forms.TextInput(attrs={"class": "w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"}),
            "nom": forms.TextInput(attrs={"class": "w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"}),
            "email": forms.EmailInput(attrs={"class": "w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"}),
            "niveau": forms.Select(attrs={"class": "w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 bg-white"}),
        }
        labels = {
            "prenom": "Prénom",
            "nom": "Nom",
            "email": "Adresse email",
            "niveau": "Classe",
        }


class MotDePasseForm(forms.Form):
    ancien = forms.CharField(
        label="Mot de passe actuel",
        widget=forms.PasswordInput(attrs={"class": "w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"}),
    )
    nouveau1 = forms.CharField(
        label="Nouveau mot de passe",
        widget=forms.PasswordInput(attrs={"class": "w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"}),
    )
    nouveau2 = forms.CharField(
        label="Confirmer le nouveau mot de passe",
        widget=forms.PasswordInput(attrs={"class": "w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"}),
    )

    def clean(self):
        cleaned = super().clean()
        n1 = cleaned.get("nouveau1", "")
        n2 = cleaned.get("nouveau2", "")
        if n1 and n2 and n1 != n2:
            raise ValidationError("Les deux nouveaux mots de passe ne correspondent pas.")
        if len(n1) < 8:
            raise ValidationError("Le nouveau mot de passe doit contenir au moins 8 caractères.")
        return cleaned
