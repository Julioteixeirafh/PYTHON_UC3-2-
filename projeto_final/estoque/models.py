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

##
# Tag
##
class Tag(models.Model):
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
    max_length=200
    )

    slug = models.SlugField(
    unique=True, 
    blank=True, 
    null=True
    )

    descricao = models.TextField(
    blank=True, 
    null=True
    )

    preco = models.DecimalField(
    max_digits=10, 
    decimal_places=2
    )

    estoque = models.PositiveIntegerField(
    default=0
    )

    ativo = models.BooleanField(
    default=True
    )

    categoria = models.ForeignKey(
        "blog.Categoria",  # se você já tem categorias no core blog
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="produtos"
    )

    criado_em = models.DateTimeField(
    auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
    auto_now=True
    )
    

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    @property
    def disponivel(self):
        return self.estoque > 0 and self.ativo