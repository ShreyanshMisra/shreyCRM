from django import forms
from .models import Lead
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput


class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class loginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class createLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['first', 'last', 'role', 'company', 'email', 'phone', 'linkedin', 'location', 'notes']


class updateLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['first', 'last', 'role', 'company', 'email', 'phone', 'linkedin', 'location', 'notes']