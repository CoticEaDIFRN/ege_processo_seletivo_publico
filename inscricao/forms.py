from django import forms
from .models import Candidato, Endereco, Inscricao

class CandidatoForm(forms.ModelForm):

    class Meta:
        model = Candidato
        fields = '__all__'


# class PagamentoForm(forms.ModelForm):
#     class Meta:
#         model = Pagamento
#         fields = ['existe_taxa', 'valor_taxa', 'vencimento_boleto']
#
# class VagaForm(forms.ModelForm):
#     class Meta:
#         model = Vaga
#         fields = '__all__'
#
# class CoordenadorForm(forms.ModelForm):
#     class Meta:
#         model = Coordenador
#         fields = '__all__'