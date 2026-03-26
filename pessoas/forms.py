from django import forms
from .models import Pessoa


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = [
            'nome_completo', 'cpf', 'rg',
            'data_nascimento', 'sexo', 'estado_civil',
            'nacionalidade', 'naturalidade', 'foto',
            'telefone', 'celular', 'email',
            'logradouro', 'numero', 'complemento',
            'bairro', 'cidade', 'estado', 'cep',
            'empresas', 'organizacoes', 'observacoes',
        ]
        widgets = {
            'nome_completo':  forms.TextInput(attrs={'class': 'form-control'}),
            'cpf':            forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'rg':             forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento':forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sexo':           forms.Select(attrs={'class': 'form-select'}),
            'estado_civil':   forms.Select(attrs={'class': 'form-select'}),
            'nacionalidade':  forms.TextInput(attrs={'class': 'form-control'}),
            'naturalidade':   forms.TextInput(attrs={'class': 'form-control'}),
            'foto':           forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'telefone':       forms.TextInput(attrs={'class': 'form-control'}),
            'celular':        forms.TextInput(attrs={'class': 'form-control'}),
            'email':          forms.EmailInput(attrs={'class': 'form-control'}),
            'logradouro':     forms.TextInput(attrs={'class': 'form-control'}),
            'numero':         forms.TextInput(attrs={'class': 'form-control'}),
            'complemento':    forms.TextInput(attrs={'class': 'form-control'}),
            'bairro':         forms.TextInput(attrs={'class': 'form-control'}),
            'cidade':         forms.TextInput(attrs={'class': 'form-control'}),
            'estado':         forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UF'}),
            'cep':            forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00000-000'}),
            'empresas':       forms.SelectMultiple(attrs={'class': 'form-select'}),
            'organizacoes':   forms.SelectMultiple(attrs={'class': 'form-select'}),
            'observacoes':    forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

from .models import Pessoa, Empresa, Organizacao


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'razao_social', 'nome_fantasia', 'cnpj', 'inscricao_estadual',
            'porte', 'situacao', 'ramo_atividade', 'data_fundacao', 'logo',
            'telefone', 'email', 'site',
            'logradouro', 'numero', 'complemento',
            'bairro', 'cidade', 'estado', 'cep',
            'observacoes',
        ]
        widgets = {
            'razao_social':       forms.TextInput(attrs={'class': 'form-control'}),
            'nome_fantasia':      forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj':               forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00.000.000/0000-00'}),
            'inscricao_estadual': forms.TextInput(attrs={'class': 'form-control'}),
            'porte':              forms.Select(attrs={'class': 'form-select'}),
            'situacao':           forms.Select(attrs={'class': 'form-select'}),
            'ramo_atividade':     forms.TextInput(attrs={'class': 'form-control'}),
            'data_fundacao':      forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'logo':               forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'telefone':           forms.TextInput(attrs={'class': 'form-control'}),
            'email':              forms.EmailInput(attrs={'class': 'form-control'}),
            'site':               forms.URLInput(attrs={'class': 'form-control'}),
            'logradouro':         forms.TextInput(attrs={'class': 'form-control'}),
            'numero':             forms.TextInput(attrs={'class': 'form-control'}),
            'complemento':        forms.TextInput(attrs={'class': 'form-control'}),
            'bairro':             forms.TextInput(attrs={'class': 'form-control'}),
            'cidade':             forms.TextInput(attrs={'class': 'form-control'}),
            'estado':             forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UF'}),
            'cep':                forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00000-000'}),
            'observacoes':        forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class OrganizacaoForm(forms.ModelForm):
    class Meta:
        model = Organizacao
        fields = [
            'nome', 'sigla', 'tipo', 'situacao',
            'area_atuacao', 'data_fundacao', 'logo',
            'organizacoes_vinculadas',
            'telefone', 'email', 'site',
            'logradouro', 'numero', 'complemento',
            'bairro', 'cidade', 'estado', 'cep',
            'observacoes',
        ]
        widgets = {
            'nome':                   forms.TextInput(attrs={'class': 'form-control'}),
            'sigla':                  forms.TextInput(attrs={'class': 'form-control'}),
            'tipo':                   forms.Select(attrs={'class': 'form-select'}),
            'situacao':               forms.Select(attrs={'class': 'form-select'}),
            'area_atuacao':           forms.TextInput(attrs={'class': 'form-control'}),
            'data_fundacao':          forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'logo':                   forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'organizacoes_vinculadas':forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
            'telefone':               forms.TextInput(attrs={'class': 'form-control'}),
            'email':                  forms.EmailInput(attrs={'class': 'form-control'}),
            'site':                   forms.URLInput(attrs={'class': 'form-control'}),
            'logradouro':             forms.TextInput(attrs={'class': 'form-control'}),
            'numero':                 forms.TextInput(attrs={'class': 'form-control'}),
            'complemento':            forms.TextInput(attrs={'class': 'form-control'}),
            'bairro':                 forms.TextInput(attrs={'class': 'form-control'}),
            'cidade':                 forms.TextInput(attrs={'class': 'form-control'}),
            'estado':                 forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UF'}),
            'cep':                    forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00000-000'}),
            'observacoes':            forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
