from django.urls import path
from . import views

app_name = 'documentos'

urlpatterns = [
    path('',                      views.documento_lista,   name='lista'),
    path('novo/',                 views.documento_criar,   name='criar'),
    path('<int:pk>/',             views.documento_detalhe, name='detalhe'),
    path('<int:pk>/editar/',      views.documento_editar,  name='editar'),
    path('<int:pk>/excluir/',     views.documento_excluir, name='excluir'),
]