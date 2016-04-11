from django import forms
from .models import Vare
from django.contrib.auth.models import User

class VareForm(forms.ModelForm):

    navn = forms.CharField(max_length=200)
    volum = forms.FloatField(max_value=10000)
    alkohol = forms.FloatField(max_value=100)
    pris = forms.FloatField(max_value=10000000)
    kalkulering = ''


    class Meta:
        model = Vare
        fields = ('navn', 'pris', 'alkohol','volum')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class TempVareForm(forms.Form):

    volum = forms.FloatField(max_value=10000)
    alkohol = forms.FloatField(max_value=100)
    pris = forms.FloatField(max_value=10000000)
    kalkulering = ''


    class Meta:
        fields = ('pris', 'alkohol','volum')