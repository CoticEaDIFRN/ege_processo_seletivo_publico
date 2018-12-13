# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, render_to_response
from .forms import EdtalForm

def novoEdital(request):
    form = EdtalForm()
    return render(request, 'cadastroEdital/edital.html', {'form': form})

# def calculate(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
    # c = EdtalForm()
    # if request.method == 'POST':
    #
    #     return HttpResponse("Hello, world. You're at the polls index.")
    # else:
    #     return render_to_response('templates/cadastroEdital/edital.html', {'aa': c})

# def novoEdital(request):
#     data = {}
#     form = EdtalForm(
#         request.POST or None)
#     # if form.is_valid():
#     #     form.save()
#     #     return redirect('novoEdital')
#
#     data['form'] = form
#
#     return render(request, 'templates/cadastroEdital/edital.html', data)
