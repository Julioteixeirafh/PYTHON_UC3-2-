from django.shortcuts import render
from django.http import HttpResponse

# A função 'home' que o Django está procurando
def home(request):
    return render(request, 'home.html')

# Suas outras views
def lista_produtos(request):
    return HttpResponse("<h1>Esta é a página de lista de produtos!</h1>")

def detalhe_produto(request, pk):
    return HttpResponse(f"<h1>Detalhes do produto {pk}</h1>")


def index(request):

    context = {
        'titulo' : 'Bem Vindo à Página de orodutos!'
    }
    
    return render(request, 'estoque/index_estoque.html', context)

    
















