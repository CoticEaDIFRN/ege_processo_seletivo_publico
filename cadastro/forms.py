from django import forms
from django.contrib.auth.models import User
from .models import Usuario


class RegistrarCadastroForm(forms.Form):

    # nome = forms.CharField(required=True)
    # email = forms.EmailField(required=True)
    # senha = forms.CharField(required=True)

    def __init__(self,  *args, **kwargs):
        super(RegistrarCadastroForm, self).__init__(*args, **kwargs)
        self.sem_erro = True

    def is_valid(self):
        if not super(RegistrarCadastroForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')

        if Usuario.objects.filter(cpf=self.data['cpf']).exists():
            self.adiciona_erro("Já existe um usuário cadastrado com este CPF.")

        if Usuario.objects.filter(email=self.data['email']).count() > 0:
            self.adiciona_erro("Já existe um usuário cadastrado com este e-Mail.")

        return self.sem_erro

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
        self.sem_erro = True
