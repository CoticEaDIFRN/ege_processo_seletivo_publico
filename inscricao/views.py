from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.views.generic.base import View
from .forms import RegistrarInscricaoForm
from python_brfied.shortcuts.sync_http import get_json
from .models import Candidato, Documento
from cadastro.models import Usuario

class RegistrarInscricaoView(View):
    template_name = 'inscricao/inscricao.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarInscricaoForm(request.POST)


        if form.is_valid():
            dados_form = form.data
            inscrito = Usuario.objects.get(cpf=dados_form['cpf'])
            inscricao = Candidato.objects.create(usuario = inscrito,
                                                 nome_civil=dados_form['nome_civil'],
                                                 nome_social=dados_form['nome_social'],
                                                 nome_apresentacao=dados_form['nome_apresentacao'],
                                                 nome_usual=dados_form['nome_usual'],
                                                 nome_mae=dados_form['nome_mae'],
                                                 nome_pai=dados_form['nome_pai'],
                                                 sexo=dados_form['sexo'],
                                                 data_nascimento=dados_form['data_nascimento'],
                                                 pais_nascimento=dados_form['pais_nascimento'],
                                                 estado_nascimento=dados_form['estado_nascimento'],
                                                 cidade_nascimento=dados_form['cidade_nascimento'],
                                                 rg=dados_form['rg'],
                                                 data_emissao=dados_form['data_emissao'],
                                                 orgao_rg=dados_form['orgao_rg'],
                                                 estado_emissao=dados_form['estado_emissao'],
                                                 email=dados_form['email'],
                                                 telefone=dados_form['telefone'],
                                                 cep=dados_form['cep'],
                                                 endereco=dados_form['endereco'],
                                                 complemento=dados_form['complemento'],
                                                 cidade=dados_form['cidade'],
                                                 estado=dados_form['estado'],
                                                 pais=dados_form['pais'],
                                                 )

            # upload = Documento.objects.create(candidato=inscrito,
            #                                   descricao=dados_form['descricao'],
            #                                   arquivo=dados_form['doc_pessoal'],
            #                                   )


            inscricao.save()
            # upload.save()

            return redirect('index')

        return render(request, self.template_name, {'form': form})

    def index(request):
        return render(request, 'inscricao/telainicial.html')

    def lista_inscricoes(request):
        return render(request, 'inscricao/listagem.html', {'inscricao': Candidato.objects.all()})