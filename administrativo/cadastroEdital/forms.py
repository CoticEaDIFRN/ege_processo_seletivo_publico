from django import forms
from .models import Edital

class EdtalForm(forms.ModelForm):

    class Meta:
        model = Edital
        fields = ['tipo', 'programa', 'numero', 'siglaUO','linkEdital','grupo', 'descricao', 'ano', 'periodo', 'data_publicacao']

