from django import forms
from .models import Candidato, Documento

class CandidatoForm(forms.ModelForm):

    class Meta:
        model = Candidato
        fields = '__all__'

class DocumentoForm(forms.ModelForm):

    class Meta:
        model = Documento
        fields = '__all__'


# class EnderecoForm(forms.ModelForm):
#
#     class Meta:
#         model = Endereco
#         fields = ['municipio', 'pais_nascimento', 'cep', 'endereco', 'complemento', 'uf', 'cidade']

# class VagaForm(forms.ModelForm):
#     class Meta:
#         model = Inscricao
#         fields = '__all__'

