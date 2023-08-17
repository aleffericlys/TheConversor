from django.urls import path 
from . import views

urlpatterns = [
  path('cripto/', views.CriptoForm, name='cripto'),
        path('obter_lista_cripto/', views.obter_lista_cripto, name='obter_lista_cripto'),
        path('obter_cotacao_cripto/', views.obter_cotacao_cripto, name='obter_cotacao_cripto'),
]	