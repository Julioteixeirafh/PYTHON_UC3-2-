from django.db import models
from django.contrib.auth.models import User # Importa o modelo de usuário padrão do Django
from PIL import Image # Importa o Image para redimensionar a imagem


# Create your models here.


class perfil(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE, 
        related_name="perfil"
    )


    cpf = models.CharField(
        max_length=14,
        unique=True, 
        null=True, 
        blank=True
    )

    telefone = models.CharField(
        max_length=15,
        null=True, 
        blank=True
    )

    data_nascimento = models.DateField(
        null=True,
        blank=True
     )

    endereco = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    numero = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )

    complemento = models.CharField(
    max_length=50,
    null=True,
    blank=True
    )

    bairro = models.CharField(
    max_length=100,
    null=True, 
    blank=True
    )

    cidade = models.CharField(
    max_length=100, 
    null=True, 
    blank=True
    )

    estado = models.CharField(
    max_length=2, 
    null=True, 
    blank=True
    )

    cep = models.CharField(
    max_length=9, 
    null=True, 
    blank=True
    )

    data_criacao = models.DateTimeField(
    auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
    auto_now=True
    )


    def __str__(self):
        return f"{self.user.username} - Perfil"