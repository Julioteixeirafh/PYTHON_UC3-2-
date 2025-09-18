from django.urls import path
from . import views 

app_name = 'estoque'

urlpatterns = [

    path( '', views.index, name = 'index'),
   # path('teste/', views.teste, name = 'este'),


    #path('', views.lista_produtos, name='lista_produtos'),

    
    #path('<int:pk>/', views.detalhe_produto, name='detalhe_produto'),
]



