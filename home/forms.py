from django import forms
from .models import Vare

class VareForm(forms.ModelForm):

    navn = forms.CharField(max_length=200)
    volum = forms.FloatField(max_value=10000)
    Alkohol = forms.FloatField(max_value=100)
    pris = forms.FloatField(max_value=10000000)

    class Meta:
        model = Vare
        fields = ('navn', 'pris', 'Alkohol','volum')