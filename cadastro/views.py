from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from .forms import RegistrarCadastroForm, RegistrarLoginForm
from .models import Usuario


class RegistrarCadastroView(View):
    template_name = 'cadastro/cadastro.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarCadastroForm(request.POST)

        if form.is_valid():
            dados_form = form.data
            usuario = Usuario.objects.create(cpf=dados_form['cpf'],
                                             nome=dados_form['nome'],
                                             email=dados_form['email'],
                                             password=dados_form['senha'])
            usuario.save()

            return redirect('index')

        return render(request, self.template_name, {'form': form})


    def index(request):

        return render(request, 'cadastro/login.html')


    def lista_cadastros(request):
        return render(request, 'cadastro/lista_cadastro.html', {'usuario': Usuario.objects.all()})


class Logar(View):
    template_name = 'cadastro/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarLoginForm(request.POST)

        if form.is_valid():
             return redirect('index')
        # else:
        #      return HttpResponse('Login inválido')



        return render(request, self.template_name, {'form': form})

    # def entrar(self, request):
    #     form = request.POST
    #
    #     if form.is_valid():
    #         dados_form = form.data
    #         if Usuario.objects.filter(email=form.data['email']).exists():
    #             password = dados_form['senha']
    #             user = authenticate(email=email, password=password)
    #             if user is not None:
    #                 login(request, user)
    #                 return HttpResponseRedirect('cadastro/index.html')
    #             else:
    #                 return HttpResponse('Login inválido')


