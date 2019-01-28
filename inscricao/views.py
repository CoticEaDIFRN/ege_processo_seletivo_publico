from django.shortcuts import render
from inscricao.forms import CandidatoForm


def nova_inscricao(request):
    form1 = CandidatoForm()
    return render(request, 'inscricao/index.html', {'form1': form1})