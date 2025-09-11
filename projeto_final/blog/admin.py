from django.contrib import admin
from .models import artigo, categoria, tag 

# Registra os modelos no painel de administração do Django
admin.site.register(artigo)
admin.site.register(categoria)
admin.site.register(tag)


















