from django import forms
from .models import Usuario

class RegistrarInscricaoForm(forms.Form):

    def __init__(self,  *args, **kwargs):
        super(RegistrarInscricaoForm, self).__init__(*args, **kwargs)
        self.sem_erro = True

    def is_valid(self):
        if not super(RegistrarInscricaoForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')

        if not Usuario.objects.filter(cpf=self.data['cpf']).exists():
            self.adiciona_erro("Não existe cadastro com o CPF informado.")

        return self.sem_erro

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
        self.sem_erro = False


class RegistrarDocumentoForm(forms.Form):

    def __init__(self,  *args, **kwargs):
        super(RegistrarDocumentoForm, self).__init__(*args, **kwargs)
        self.sem_erro = True

    def is_valid(self):
        if not super(RegistrarDocumentoForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')

        return self.sem_erro

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
        self.sem_erro = False



# class CandidatoForm(forms.ModelForm):
#
#     class Meta:
#         model = Candidato
#         fields = '__all__'
#
# class DocumentoForm(forms.ModelForm):
#
#     class Meta:
#         model = Documento
#         fields = '__all__'


# class EnderecoForm(forms.ModelForm):
#
#     class Meta:
#         model = Endereco
#         fields = ['municipio', 'pais_nascimento', 'cep', 'endereco', 'complemento', 'uf', 'cidade']

# class VagaForm(forms.ModelForm):
#     class Meta:
#         model = Inscricao
#         fields = '__all__'