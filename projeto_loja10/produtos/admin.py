# produtos/admin.py

from django.contrib import admin
from .models import Produto # <-- Importa o modelo Produto da sua aplicação

# Registra o modelo Produto
#admin.site.register(Produto)->registro default


# Define uma classe ModelAdmin para o modelo Produto
class ProdutoAdmin(admin.ModelAdmin):
    # Campos que serão exibidos na página de lista de objetos
    list_display = ('nome', 'preco', 'quantidade', 'status')
    
    # Campos que podem ser clicados para ordenar a lista
    list_display_links = ('nome',)
    
    # Adiciona uma barra lateral de filtro para os campos
    list_filter = ('status', 'data_criacao') # Supondo que você tenha um campo data_criacao
    
    # Adiciona uma barra de pesquisa
    search_fields = ('nome', 'descricao') # Pesquisa por nome ou descrição
    
    # Permite editar campos diretamente na lista (cuidado com isso em produção!)
    list_editable = ('preco', 'quantidade', 'status')
    
    # Pre-popula o campo 'slug' (se você tiver um) baseado no 'nome'
    # prepopulated_fields = {'slug': ('nome',)}
    
    # Agrupa campos no formulário de edição/criação
    fieldsets = (
        (None, {
            'fields': ('nome', 'descricao', 'preco', 'quantidade', 'status', 'imagem')
        }),
    )

# Registra o modelo Produto com a sua classe ModelAdmin personalizada
admin.site.register(Produto, ProdutoAdmin)