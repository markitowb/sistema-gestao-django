from django.urls import path
from . import views

app_name = 'registros'

urlpatterns = [
    # Fatos
    path('fatos/',                       views.fato_lista,           name='fato_lista'),
    path('fatos/novo/',                  views.fato_criar,           name='fato_criar'),
    path('fatos/<int:pk>/',              views.fato_detalhe,         name='fato_detalhe'),
    path('fatos/<int:pk>/editar/',       views.fato_editar,          name='fato_editar'),
    path('fatos/<int:pk>/excluir/',      views.fato_excluir,         name='fato_excluir'),

    # Relatórios
    path('relatorios/',                  views.relatorio_lista,      name='relatorio_lista'),
    path('relatorios/novo/',             views.relatorio_criar,      name='relatorio_criar'),
    path('relatorios/<int:pk>/',         views.relatorio_detalhe,    name='relatorio_detalhe'),
    path('relatorios/<int:pk>/editar/',  views.relatorio_editar,     name='relatorio_editar'),
    path('relatorios/<int:pk>/excluir/', views.relatorio_excluir,    name='relatorio_excluir'),

    # Memórias
    path('memorias/',                    views.memoria_lista,        name='memoria_lista'),
    path('memorias/novo/',               views.memoria_criar,        name='memoria_criar'),
    path('memorias/<int:pk>/',           views.memoria_detalhe,      name='memoria_detalhe'),
    path('memorias/<int:pk>/editar/',    views.memoria_editar,       name='memoria_editar'),
    path('memorias/<int:pk>/excluir/',   views.memoria_excluir,      name='memoria_excluir'),
]