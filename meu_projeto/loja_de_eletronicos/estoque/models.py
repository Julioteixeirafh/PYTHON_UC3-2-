from django.db import models


##
# Categoria
##
class Categoria(models.Model):
    identificacao = models.CharField(max_length=100, 
        verbose_name="Identificacao", 
        help_text="Informe a identificação da categoria",
        unique=True,
    )
    
    descricao = models.TextField (
        verbose_name="Descrição",
        help_text="Informe a descrição da categoria",
        default="N/A",
    )
    
    def __str__(self):
        return self.identificacao
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    data_criacao = models.DateTimeField(
        verbose_name="Data de criação",
        auto_now_add=True
    )
    

##
# Tag
##
class Protuto_Tag(models.Model):
    identificacao = models.CharField(max_length=100, 
        verbose_name="Identificacao", 
        help_text="Informe a identificação da tag",
        unique=True)
    
    descricao = models.TextField (
        verbose_name="Descrição",
        help_text="Informe a descrição da categoria",
        default="N/A",
    )
    
    def __str__(self):
        return self.identificacao
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
##
# Produto
##
class Produto(models.Model):
    nome = models.CharField(
        max_length=100,
        verbose_name="Nome do produto",
        help_text="Nome do produto"
        )
    
    descricao = models.TextField(
        verbose_name="Descrição",
        help_text="Descrição detalhada do produto",
        default="N/A"
        )
    
    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Preço",
        help_text="Preço de venda do produto",
        default=0.0
    )
    
    estoque = models.PositiveIntegerField(
        default=0, 
        verbose_name="Qt de produtos",
        help_text="Quantidade do produto em estoque"
    )

    disponivel = models.BooleanField(        
        default=True, 
        verbose_name="Produto Disponivel",
        help_text="Indica se o produto está disponível para venda"
    )
    
    imagem = models.ImageField(
        upload_to='produtos/', 
        blank=True, 
        null=True, 
        help_text="Imagem de exibição do produto"
    )

    # Campos de data
    data_criacao = models.DateTimeField(
        verbose_name="Data de criação",
        auto_now_add=True
    )
    
    data_atualizacao = models.DateTimeField(
        verbose_name="Data de atualização",
        auto_now=True
    )
   

    # Aqui está a relação! Cada produto pertence a uma categoria. (Aula 11.02.02)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,  # <-- Permite que o valor no banco de dados seja NULO
        blank=True, # <-- Permite que o campo no admin/formulários fique em branco 
        related_name="produtos"
    )
    
    tag = models.ManyToManyField (
        Protuto_Tag,
        related_name="produto_tags"
    )
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome']


        ##
# Pedido
##
class Pedido(models.Model):
    FORMA_PAGAMENTO_CHOICES = [
        ('PIX', 'PIX'),
        ('CARTAO', 'Cartão de Crédito'),
        ('BOLETO', 'Boleto Bancário'),
    ]
    
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('CONFIRMADO', 'Confirmado'),
        ('CANCELADO', 'Cancelado'),
    ]
    
    # Dados do cliente
    nome_cliente = models.CharField(max_length=200, verbose_name="Nome Completo")
    email_cliente = models.EmailField(verbose_name="E-mail")
    telefone_cliente = models.CharField(max_length=20, verbose_name="Telefone")
    cpf_cliente = models.CharField(max_length=14, verbose_name="CPF")
    
    # Endereço
    cep = models.CharField(max_length=9, verbose_name="CEP")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    numero = models.CharField(max_length=10, verbose_name="Número")
    complemento = models.CharField(max_length=100, blank=True, verbose_name="Complemento")
    bairro = models.CharField(max_length=100, verbose_name="Bairro")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    estado = models.CharField(max_length=2, verbose_name="Estado")
    
    # Dados do pedido
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="pedidos")
    quantidade = models.PositiveIntegerField(default=1, verbose_name="Quantidade")
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Total")
    
    forma_pagamento = models.CharField(
        max_length=10,
        choices=FORMA_PAGAMENTO_CHOICES,
        verbose_name="Forma de Pagamento"
    )
    
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='PENDENTE',
        verbose_name="Status"
    )
    
    data_pedido = models.DateTimeField(auto_now_add=True, verbose_name="Data do Pedido")
    
    def __str__(self):
        return f"Pedido #{self.id} - {self.nome_cliente}"
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['-data_pedido']