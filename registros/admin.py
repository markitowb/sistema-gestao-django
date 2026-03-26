from django.contrib import admin
from .models import Fato, Relatorio, Memoria

# Register your models here.

@admin.register(Fato)
class FatoAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'tipo', 'data_fato', 'local', 'confidencial', 'criado_por')
    search_fields = ('titulo', 'descricao', 'fonte')
    list_filter   = ('tipo', 'confidencial')
    filter_horizontal = ('pessoas', 'empresas', 'organizacoes', 'documentos')

@admin.register(Relatorio)
class RelatorioAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'data_referencia', 'criado_por', 'criado_em')
    search_fields = ('titulo', 'conteudo')
    filter_horizontal = ('pessoas', 'empresas', 'fatos', 'documentos')

@admin.register(Memoria)
class MemoriaAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'fixada', 'data_memoria', 'criado_por', 'criado_em')
    search_fields = ('titulo', 'conteudo')
    list_filter   = ('fixada',)
    filter_horizontal = ('pessoas', 'empresas', 'organizacoes')