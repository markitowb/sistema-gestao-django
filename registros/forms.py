from django import forms
from .models import Fato, Relatorio, Memoria


class FatoForm(forms.ModelForm):
    class Meta:
        model = Fato
        fields = [
            'titulo', 'tipo', 'descricao', 'data_fato',
            'local', 'fonte', 'confidencial',
            'pessoas', 'empresas', 'organizacoes', 'documentos',
        ]
        widgets = {
            'titulo':       forms.TextInput(attrs={'class': 'form-control'}),
            'tipo':         forms.Select(attrs={'class': 'form-select'}),
            'descricao':    forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'data_fato':    forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'local':        forms.TextInput(attrs={'class': 'form-control'}),
            'fonte':        forms.TextInput(attrs={'class': 'form-control'}),
            'confidencial': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pessoas':      forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
            'empresas':     forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
            'organizacoes': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
            'documentos':   forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
        }


class RelatorioForm(forms.ModelForm):
    class Meta:
        model = Relatorio
        fields = [
            'titulo', 'conteudo', 'data_referencia',
            'pessoas', 'empresas', 'organizacoes',
            'fatos', 'documentos',
        ]
        widgets = {
            'titulo':          forms.TextInput(attrs={'class': 'form-control'}),
            'conteudo':        forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'data_referencia': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'pessoas':         forms.SelectMultiple(attrs={'class': 'form-select', 'size': '4'}),
            'empresas':        forms.SelectMultiple(attrs={'class': 'form-select', 'size': '4'}),
            'organizacoes':    forms.SelectMultiple(attrs={'class': 'form-select', 'size': '4'}),
            'fatos':           forms.SelectMultiple(attrs={'class': 'form-select', 'size': '4'}),
            'documentos':      forms.SelectMultiple(attrs={'class': 'form-select', 'size': '4'}),
        }


class MemoriaForm(forms.ModelForm):
    class Meta:
        model = Memoria
        fields = [
            'titulo', 'conteudo', 'data_memoria', 'fixada',
            'pessoas', 'empresas', 'organizacoes',
        ]
        widgets = {
            'titulo':       forms.TextInput(attrs={'class': 'form-control'}),
            'conteudo':     forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'data_memoria': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fixada':       forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pessoas':      forms.SelectMultiple(attrs={'class': 'form-select', 'size': '4'}),
            'empresas':     forms.SelectMultiple(attrs={'class': 'form-select', 'size': '4'}),
            'organizacoes': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '4'}),
        }

