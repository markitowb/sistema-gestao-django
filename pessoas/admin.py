from django.contrib import admin
from .models import Pessoa, Empresa, Organizacao

# Register your models here.



@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display  = ('nome_completo', 'cpf', 'telefone', 'cidade', 'estado', 'criado_em')
    search_fields = ('nome_completo', 'cpf', 'email', 'telefone')
    list_filter   = ('sexo', 'estado_civil', 'estado')
    filter_horizontal = ('empresas', 'organizacoes')


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display  = ('razao_social', 'nome_fantasia', 'cnpj', 'situacao', 'cidade', 'estado')
    search_fields = ('razao_social', 'nome_fantasia', 'cnpj')
    list_filter   = ('situacao', 'porte', 'estado')


@admin.register(Organizacao)
class OrganizacaoAdmin(admin.ModelAdmin):
    list_display  = ('nome', 'sigla', 'tipo', 'situacao', 'cidade', 'estado')
    search_fields = ('nome', 'sigla')
    list_filter   = ('tipo', 'situacao', 'estado')
