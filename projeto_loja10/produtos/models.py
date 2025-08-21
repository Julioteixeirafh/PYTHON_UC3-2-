# produtos/models.py (aula 10)

from django.db import models

##
# Primeira versão do model adicionado na aula 10
##
class Produto(models.Model):
    nome = models.CharField(
        max_length=100
        )

    descricao = models.TextField(

    )

    tipo = models.CharField(
        max_length=50,
        blank=True,
        null=True,

    )

    fabricante = models.CharField(
        max_length=60,
        blank=True,
        null=True,
    )

    modelo = models.CharField(
        max_length=51,
        blank=True,
        null=True,
    )

    quantidade = models.PositiveIntegerField(
        default=0
    )

    status = models.BooleanField(
        default=True,
    )

    data_criacao = models.DateTimeField(
        auto_now_add=True
    )

    data_atualizacao = models.DateTimeField(
        auto_now=True
    )

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    imagem = models.ImageField(upload_to='produtos/',
    blank=True,
    null=True
    )

    def __str__(self):
        return self.nome