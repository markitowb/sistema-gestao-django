from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Pessoa
from .forms import PessoaForm

# ── Função Home (Dashboard) ──────────────────────────────────────────────────
@login_required
def home(request):
    from documentos.models import Documento
    from registros.models import Fato, Relatorio, Memoria

    contexto = {
        # Totais
        'total_pessoas':      Pessoa.objects.count(),
        'total_empresas':     Empresa.objects.count(),
        'total_organizacoes': Organizacao.objects.count(),
        'total_documentos':   Documento.objects.count(),
        'total_fatos':        Fato.objects.count(),
        'total_relatorios':   Relatorio.objects.count(),
        'total_memorias':     Memoria.objects.count(),

        # Atividade recente
        'pessoas_recentes':   Pessoa.objects.order_by('-criado_em')[:5],
        'fatos_recentes':     Fato.objects.order_by('-data_fato')[:5],
        'docs_recentes':      Documento.objects.order_by('-criado_em')[:5],
        'memorias_fixadas':   Memoria.objects.filter(fixada=True).order_by('-criado_em')[:3],
    }
    return render(request, 'home.html', contexto)


# ── Listagem ──────────────────────────────────────────────────
@login_required
def pessoa_lista(request):
    query = request.GET.get('q', '')
    pessoas = Pessoa.objects.all().order_by('nome_completo')

    if query:
        pessoas = pessoas.filter(nome_completo__icontains=query)

    return render(request, 'pessoas/lista.html', {
        'pessoas': pessoas,
        'query': query,
    })


# ── Detalhe ───────────────────────────────────────────────────
@login_required
def pessoa_detalhe(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    return render(request, 'pessoas/detalhe.html', {'pessoa': pessoa})


# ── Cadastrar ─────────────────────────────────────────────────
@login_required
def pessoa_criar(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pessoa cadastrada com sucesso!')
            return redirect('pessoas:lista')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = PessoaForm()

    return render(request, 'pessoas/form.html', {
        'form': form,
        'titulo': 'Cadastrar Pessoa',
    })


# ── Editar ────────────────────────────────────────────────────
@login_required
def pessoa_editar(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)

    if request.method == 'POST':
        form = PessoaForm(request.POST, request.FILES, instance=pessoa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pessoa atualizada com sucesso!')
            return redirect('pessoas:detalhe', pk=pessoa.pk)
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = PessoaForm(instance=pessoa)

    return render(request, 'pessoas/form.html', {
        'form': form,
        'titulo': f'Editar — {pessoa.nome_completo}',
        'pessoa': pessoa,
    })


# ── Excluir ───────────────────────────────────────────────────
@login_required
def pessoa_excluir(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)

    if request.method == 'POST':
        nome = pessoa.nome_completo
        pessoa.delete()
        messages.success(request, f'"{nome}" foi excluído com sucesso.')
        return redirect('pessoas:lista')

    return render(request, 'pessoas/confirmar_exclusao.html', {'pessoa': pessoa})

from .models import Pessoa, Empresa, Organizacao
from .forms import PessoaForm, EmpresaForm, OrganizacaoForm


# ══════════════════════════════════════════════
# EMPRESAS
# ══════════════════════════════════════════════

@login_required
def empresa_lista(request):
    query = request.GET.get('q', '')
    empresas = Empresa.objects.all().order_by('razao_social')
    if query:
        empresas = empresas.filter(razao_social__icontains=query)
    return render(request, 'pessoas/empresa_lista.html', {
        'empresas': empresas, 'query': query,
    })


@login_required
def empresa_detalhe(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    return render(request, 'pessoas/empresa_detalhe.html', {'empresa': empresa})


@login_required
def empresa_criar(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empresa cadastrada com sucesso!')
            return redirect('pessoas:empresa_lista')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = EmpresaForm()
    return render(request, 'pessoas/empresa_form.html', {
        'form': form, 'titulo': 'Cadastrar Empresa',
    })


@login_required
def empresa_editar(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES, instance=empresa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empresa atualizada com sucesso!')
            return redirect('pessoas:empresa_detalhe', pk=empresa.pk)
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'pessoas/empresa_form.html', {
        'form': form, 'titulo': f'Editar — {empresa}', 'empresa': empresa,
    })


@login_required
def empresa_excluir(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        nome = str(empresa)
        empresa.delete()
        messages.success(request, f'"{nome}" excluída com sucesso.')
        return redirect('pessoas:empresa_lista')
    return render(request, 'pessoas/empresa_confirmar_exclusao.html', {'empresa': empresa})


# ══════════════════════════════════════════════
# ORGANIZAÇÕES
# ══════════════════════════════════════════════

@login_required
def organizacao_lista(request):
    query = request.GET.get('q', '')
    organizacoes = Organizacao.objects.all().order_by('nome')
    if query:
        organizacoes = organizacoes.filter(nome__icontains=query)
    return render(request, 'pessoas/organizacao_lista.html', {
        'organizacoes': organizacoes, 'query': query,
    })


@login_required
def organizacao_detalhe(request, pk):
    organizacao = get_object_or_404(Organizacao, pk=pk)
    return render(request, 'pessoas/organizacao_detalhe.html', {'organizacao': organizacao})


@login_required
def organizacao_criar(request):
    if request.method == 'POST':
        form = OrganizacaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Organização cadastrada com sucesso!')
            return redirect('pessoas:organizacao_lista')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = OrganizacaoForm()
    return render(request, 'pessoas/organizacao_form.html', {
        'form': form, 'titulo': 'Cadastrar Organização',
    })


@login_required
def organizacao_editar(request, pk):
    organizacao = get_object_or_404(Organizacao, pk=pk)
    if request.method == 'POST':
        form = OrganizacaoForm(request.POST, request.FILES, instance=organizacao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Organização atualizada com sucesso!')
            return redirect('pessoas:organizacao_detalhe', pk=organizacao.pk)
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = OrganizacaoForm(instance=organizacao)
    return render(request, 'pessoas/organizacao_form.html', {
        'form': form, 'titulo': f'Editar — {organizacao}', 'organizacao': organizacao,
    })


@login_required
def organizacao_excluir(request, pk):
    organizacao = get_object_or_404(Organizacao, pk=pk)
    if request.method == 'POST':
        nome = str(organizacao)
        organizacao.delete()
        messages.success(request, f'"{nome}" excluída com sucesso.')
        return redirect('pessoas:organizacao_lista')
    return render(request, 'pessoas/organizacao_confirmar_exclusao.html', {'organizacao': organizacao})

