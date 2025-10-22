from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Produto, Protuto_Tag, Categoria

def teste(request):
    """
    Esta função é a nossa view 'index'.
    Ela será responsável por exibir a página inicial da aplicação produtos.
    """
    
    # Criamos um dicionário com dados que queremos enviar para o template.
    # Por enquanto, vamos enviar um título simples.
    context = {
        'titulo': 'Bem-vindo à Página de Produtos!'
    }

    # A função render 'junta' o template com os dados e retorna uma resposta HTTP.
    return render(request, 'estoque/index_static.html', context)


def index(request):
    """
    Esta função é a nossa view 'index'.
    Ela será responsável por exibir a página inicial da aplicação produtos.
    """
    
    # Criamos um dicionário com dados que queremos enviar para o template.
    # Por enquanto, vamos enviar um título simples.
    context = {
        'titulo': 'Bem-vindo à Página de Produtos!'
    }

    # A função render 'junta' o template com os dados e retorna uma resposta HTTP.
    return render(request, 'estoque/index_estoque.html', context)

##
# Produtos
##
class ProdutoListView(ListView):
    model = Produto
    template_name = 'estoque/produto_list.html'
    context_object_name = 'produtos'  # Nome da variável a ser usada no template
    ordering = ['nome']  # Opcional: ordena os produtos por nome
    #paginate_by = 10 # Opcional: Adiciona paginação


class ProdutoTabelaListView(ListView):
    model = Produto
    template_name = 'estoque/produto_tabela_list.html'
    context_object_name = 'produtos'  # Nome da variável a ser usada no template
    ordering = ['nome']  # Opcional: ordena os produtos por nome
    paginate_by = 10 # Opcional: Adiciona paginação


# READ (Detail)
class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'estoque/produto_detail.html'
    context_object_name = 'produto'

# CREATE
class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'estoque/produto_form.html'
    # Lista dos campos que o usuário poderá preencher
    fields = ['nome', 'descricao', 'preco', 'estoque', 'disponivel', 'imagem', 'categoria', 'tag']
    # URL para onde o usuário será redirecionado após o sucesso
    success_url = reverse_lazy('estoque:produto_list')

    # Adiciona um título dinâmico ao contexto do template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Cadastrar Novo Produto'
        return context


class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'estoque/categoria_form.html'
    # Lista dos campos que o usuário poderá preencher
    fields = ['identificacao', 'descricao', 'categoria',]
    # URL para onde o usuário será redirecionado após o sucesso
    success_url = reverse_lazy('estoque:categoria_list')

    # Adiciona um título dinâmico ao contexto do template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Cadastrar Novo Produto'
        return context



# UPDATE
class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'estoque/produto_form.html'
    fields = ['nome', 'descricao', 'preco', 'estoque', 'disponivel', 'imagem', 'categoria', 'tag']
    success_url = reverse_lazy('estoque:produto_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Editar Produto'
        return context

# DELETE
class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'estoque/produto_confirm_delete.html'
    success_url = reverse_lazy('estoque:produto_list')
    context_object_name = 'produto'





class CategoriaListView(ListView):
    model = Categoria
    template_name = 'estoque/categoria/categoria_list.html' 
    context_object_name = 'categorias'  # Nome da variável a ser usada no template
    ordering = ['identificacao']  # Opcional: ordena os produtos por nome
    #paginate_by = 10 # Opcional: Adiciona paginação

# READ (Detail)
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'estoque/categoria/categoria_detail.html'
    context_object_name = 'categoria'





class TagListView(ListView):
    model = Protuto_Tag
    template_name = 'estoque/tag/tag_list.html'
    context_object_name = 'tags'  # Nome da variável a ser usada no template
    ordering = ['identificacao']  # Opcional: ordena os produtos por nome
    #paginate_by = 10 # Opcional: Adiciona paginação


# READ (Detail)
class TagDetailView(DetailView):
    model = Protuto_Tag
    template_name = 'estoque/tag/tag_detail.html'
    context_object_name = 'tag'


from django.views.generic import TemplateView
from .models import Pedido
from django.shortcuts import get_object_or_404, redirect



##
# Checkout e Pagamento
##
class CheckoutView(CreateView):
    model = Pedido
    template_name = 'estoque/checkout.html'
    fields = ['nome_cliente', 'email_cliente', 'telefone_cliente', 'cpf_cliente', 
              'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'quantidade']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produto'] = get_object_or_404(Produto, pk=self.kwargs['pk'])
        return context
    
    def form_valid(self, form):
        produto = get_object_or_404(Produto, pk=self.kwargs['pk'])
        pedido = form.save(commit=False)
        pedido.produto = produto
        pedido.valor_total = produto.preco * pedido.quantidade
        pedido.save()
        return redirect('estoque:pagamento', pedido_id=pedido.id)


class PagamentoView(UpdateView):
    model = Pedido
    template_name = 'estoque/pagamento.html'
    fields = ['forma_pagamento']
    pk_url_kwarg = 'pedido_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pedido'] = self.object
        return context
    
    def get_success_url(self):
        return reverse_lazy('estoque:confirmacao', kwargs={'pedido_id': self.object.id})


class ConfirmacaoView(DetailView):
    model = Pedido
    template_name = 'estoque/confirmacao.html'
    pk_url_kwarg = 'pedido_id'
    context_object_name = 'pedido'




