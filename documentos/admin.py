from django.contrib import admin
from .models import Documento

# Register your models here.

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'tipo', 'categoria', 'data_documento', 'criado_por', 'criado_em')
    search_fields = ('titulo', 'descricao')
    list_filter   = ('tipo', 'categoria')
    filter_horizontal = ('pessoas', 'empresas', 'organizacoes')