from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Livre
from django_summernote.widgets import SummernoteWidget

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta :
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre', 'auteur', 'isbn', 'description', 'date_publication']
        widgets = {
            'date_publication': forms.DateInput(attrs={'type': 'date'}),
            'description': SummernoteWidget(attrs={'placeholder': 'Description (facultatif)'}),
            'isbn': forms.TextInput(attrs={'placeholder': 'Facultatif'}),
        }
        labels = {
            'isbn': 'ISBN',
        }