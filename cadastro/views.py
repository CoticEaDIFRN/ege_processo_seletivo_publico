from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.base import View
from inscricao.models import Candidato
from .forms import RegistrarCadastroForm
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
        return render(request, 'cadastro/index.html')


    def lista_cadastros(request):
        return render(request, 'cadastro/lista_cadastro.html', {'usuario': Usuario.objects.all()})