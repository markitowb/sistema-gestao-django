from django.urls import path
from . import views

app_name = 'pessoas'

urlpatterns = [
    #Home
    path('',                      views.home,            name='home'),

    #Pessoas
    path('pessoas/',              views.pessoa_lista,    name='lista'),
    path('pessoas/novo/',         views.pessoa_criar,    name='criar'),
    path('pessoas/<int:pk>/',     views.pessoa_detalhe,  name='detalhe'),
    path('pessoas/<int:pk>/editar/',  views.pessoa_editar,   name='editar'),
    path('pessoas/<int:pk>/excluir/', views.pessoa_excluir,  name='excluir'),

    # Empresas
    path('empresas/',                     views.empresa_lista,   name='empresa_lista'),
    path('empresas/novo/',                views.empresa_criar,   name='empresa_criar'),
    path('empresas/<int:pk>/',            views.empresa_detalhe, name='empresa_detalhe'),
    path('empresas/<int:pk>/editar/',     views.empresa_editar,  name='empresa_editar'),
    path('empresas/<int:pk>/excluir/',    views.empresa_excluir, name='empresa_excluir'),

    # Organizações
    path('organizacoes/',                 views.organizacao_lista,   name='organizacao_lista'),
    path('organizacoes/novo/',            views.organizacao_criar,   name='organizacao_criar'),
    path('organizacoes/<int:pk>/',        views.organizacao_detalhe, name='organizacao_detalhe'),
    path('organizacoes/<int:pk>/editar/', views.organizacao_editar,  name='organizacao_editar'),
    path('organizacoes/<int:pk>/excluir/',views.organizacao_excluir, name='organizacao_excluir'),
]