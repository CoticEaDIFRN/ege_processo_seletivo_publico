from django.shortcuts import render
from inscricao.forms import CandidatoForm, PagamentoForm


def nova_inscricao(request):
    form1 = CandidatoForm()
    form2 = PagamentoForm()
    return render(request, 'inscricao/index.html', {'form1': form1, 'form2': form2})