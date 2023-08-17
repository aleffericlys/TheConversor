from django.urls import path 
from . import views

urlpatterns = [
        path('moedas/', views.MoedasForm, name='moedas'),
        path('obter_lista_moedas/', views.obter_lista_moedas, name='obter_lista_moedas'),
        path('obter_cotacao/', views.obter_cotacao, name='obter_cotacao'),
]	