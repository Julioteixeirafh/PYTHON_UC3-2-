from django.shortcuts import render
from djanngo.urls import reverse_lazy
drom django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)

from models

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'produtos/index.html', {'title': 'Home'})

def produtos(request):
    return render(request, 'produtos/produtos.html', {'title': 'Produtos'})

def contato(request):
    return render(request, 'produtos/contato.html', {'title': 'Contato'})


    