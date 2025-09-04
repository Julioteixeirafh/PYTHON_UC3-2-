from django.db import models
from django.contrib.auth.models import User # Importa o modelo de usuário padrão do Django
from PIL import Image # Importa o Image para redimensionar a imagem

# Create your models here.

class artigo(models.Model):

    titulo = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        unique=True, 
        blank=True, 
        null=True
    )

    autor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="artigos"
    )

    conteudo = models.TextField()

    imagem_destaque = models.ImageField(
        upload_to="artigos/", 
        null=True, 
        blank=True
    )

    publicado = models.BooleanField(
        default=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )


    class Meta:
        ordering = ["-criado_em"]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)



class tag(models.Model):

    nome = models.CharField(
    max_length=50, 
    unique=True
    )

    slug = models.SlugField(
    max_length=60, 
    unique=True,
    blank=True, 
    null=True
    )

    criado_em = models.DateTimeField(
    auto_now_add=True
    )


    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)



class categoria(models.Model):

    nome = models.CharField(
    max_length=100, 
    unique=True
    )

    slug = models.SlugField(
    max_length=120, 
    unique=True, 
    blank=True, 
    null=True
    )

    descricao = models.TextField(
    blank=True, 
    null=True
    )

    ativa = models.BooleanField(
    default=True
    )

    pai = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="subcategorias"
    )

    criado_em = models.DateTimeField(
    auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
    auto_now=True
    )


    class Meta:
        ordering = ["nome"]
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)