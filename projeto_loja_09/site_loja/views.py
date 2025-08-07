# core/site/views.py
from django.shortcuts import render

def home(request):
    """
    View para a página inicial do site.
    """
    return render(request, 'site_loja/home.html')

##
# Versão Original
##
def lista_produtos_v1(request):
    """
    View para listar os produtos.
    """
    context = {
        'produtos': '',
        'titulo': 'Bem-vindo à Página de Produtos!'
    }
    return render(request, 'site_loja/lista_produtos.html', context)

##
# Versão - Aula 09
##
def produtos_lista(request):
    # Lógica para obter a lista de produtos
    produtos = [
        {'nome': 'Smartphone X', 'preco': 1500},
        {'nome': 'Notebook Y', 'preco': 3000},
        {'nome': 'Fone de Ouvido Z', 'preco': 200},
    ]
    titulo: 'Bem-vindo à Página de Produtos!'
    return render(request, 'site_loja/produtos_lista.html', {'produtos': produtos})