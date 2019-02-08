from django.shortcuts import render, redirect
from inscricao.forms import CandidatoForm
from .models import Candidato

def nova_inscricao(request):
    data = {}
    form1 = CandidatoForm(request.POST or None)

    if form1.is_valid():
        form1.save()
        return listagem(request)

    data['form1'] = form1

    return render(request, 'inscricao/index.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Candidato.objects.all()
    return render(request, 'inscricao/listagem.html', data)