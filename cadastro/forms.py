from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from .models import Usuario


class RegistrarCadastroForm(forms.Form):


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

        if self.data['senha'] != self.data['senha2']:
            self.adiciona_erro("Senhas não correspondem.")

        return self.sem_erro

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
        self.sem_erro = False



# class RegistrarLoginForm(forms.Form):
#
#    def __init__(self,  *args, **kwargs):
#         super(RegistrarLoginForm, self).__init__(*args, **kwargs)
#         self.sem_erro = True
#
#    def is_valid(self):
#         if not super(RegistrarLoginForm, self).is_valid():
#             self.adiciona_erro('Por favor, verifique os dados informados')
#
#         if Usuario.objects.filter(email=self.data['email']).count() == 0:
#             self.adiciona_erro("Email não cadastrado.")
#
#         return self.sem_erro
#
#
#    def adiciona_erro(self, message):
#         errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
#         errors.append(message)
#         self.sem_erro = False


