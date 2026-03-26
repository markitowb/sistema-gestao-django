from django import forms
from .models import Documento


class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
            'titulo', 'tipo', 'categoria', 'descricao',
            'arquivo', 'data_documento',
            'pessoas', 'empresas', 'organizacoes',
        ]
        widgets = {
            'titulo':         forms.TextInput(attrs={'class': 'form-control'}),
            'tipo':           forms.Select(attrs={'class': 'form-select'}),
            'categoria':      forms.Select(attrs={'class': 'form-select'}),
            'descricao':      forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'arquivo':        forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'data_documento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'pessoas':        forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
            'empresas':       forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
            'organizacoes':   forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
        }

