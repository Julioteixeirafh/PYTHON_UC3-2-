# imports
from django.urls import path 

# Importamos as views da nossa aplicação (o arquivo views.py)
from . import views          

# Define o "namespace" para a aplicação
app_name = 'estoque' 

urlpatterns = [
    # O caminho vazio '' significa a raiz da nossa aplicação 'produtos'
    path('', views.index, name='index'),
    path('teste/', views.teste, name='este'),

    ##
    # Produtos
    ##
    path('produtos/', views.ProdutoListView.as_view(), name='produto_list'),
    path('produtos/listar/', views.ProdutoTabelaListView.as_view(), name='produto_tabela_list'),
    path('produtos/<int:pk>/', views.ProdutoDetailView.as_view(), name='produto_detail'),
    path('produtos/novo/', views.ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<int:pk>/editar/', views.ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/<int:pk>/deletar/', views.ProdutoDeleteView.as_view(), name='produto_delete'),

    path('categoria/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categoria/novo/', views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categoria/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria_detail'),
    path('categoria/<int:pk>/editar/', views.CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categoria/<int:pk>/deletar/', views.CategoriaDeleteView.as_view(), name='categoria_delete'),


    path('tag/', views.TagListView.as_view(), name='tag_list'),
    path('tag/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),

    path('checkout/<int:pk>/', views.CheckoutView.as_view(), name='checkout'),
    path('pagamento/<int:pedido_id>/', views.PagamentoView.as_view(), name='pagamento'),
    path('confirmacao/<int:pedido_id>/', views.ConfirmacaoView.as_view(), name='confirmacao'),

]