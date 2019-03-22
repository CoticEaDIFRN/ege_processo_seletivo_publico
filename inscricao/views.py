from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from python_brfied.shortcuts.sync_http import get_json
from inscricao.forms import CandidatoForm, DocumentoForm
from .models import Candidato

def nova_inscricao(request):
    data = {}
    form1 = CandidatoForm(request.POST or None)
    form2 = DocumentoForm(request.POST or None)
    if form1.is_valid() and form2.is_valid():
        form1.save()
        form2.save()
        return listagem(request)

    data['form1'] = form1
    data['form2'] = form2

    return render(request, 'inscricao/inscricao.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Candidato.objects.all()
    return render(request, 'inscricao/listagem.html', data)

# def authenticate_credentials(request):
    # result= {}
    # result['candidato'] = get_json('http://acesso:8000/ege/selecao/api/v1/candidato/%s/')
    # return render(request, 'inscricao/telainicial.html', result)

def cadastro(request):
    return render(request, 'inscricao/cadastro.html')