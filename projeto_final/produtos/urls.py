from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/', views.produtos, name='produtos'),
    path('contato/', views.contato, name='contato'),
]

