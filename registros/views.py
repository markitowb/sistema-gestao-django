from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Fato, Relatorio, Memoria
from .forms import FatoForm, RelatorioForm, MemoriaForm


# ══════════════════════════════════════════════
# FATOS
# ══════════════════════════════════════════════

@login_required
def fato_lista(request):
    query = request.GET.get('q', '')
    fatos = Fato.objects.all().order_by('-data_fato')
    if query:
        fatos = fatos.filter(titulo__icontains=query)
    return render(request, 'registros/fato_lista.html', {
        'fatos': fatos, 'query': query,
    })


@login_required
def fato_detalhe(request, pk):
    fato = get_object_or_404(Fato, pk=pk)
    return render(request, 'registros/fato_detalhe.html', {'fato': fato})


@login_required
def fato_criar(request):
    if request.method == 'POST':
        form = FatoForm(request.POST)
        if form.is_valid():
            fato = form.save(commit=False)
            fato.criado_por = request.user
            fato.save()
            form.save_m2m()
            messages.success(request, 'Fato registrado com sucesso!')
            return redirect('registros:fato_lista')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = FatoForm()
    return render(request, 'registros/fato_form.html', {
        'form': form, 'titulo': 'Registrar Fato',
    })


@login_required
def fato_editar(request, pk):
    fato = get_object_or_404(Fato, pk=pk)
    if request.method == 'POST':
        form = FatoForm(request.POST, instance=fato)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fato atualizado com sucesso!')
            return redirect('registros:fato_detalhe', pk=fato.pk)
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = FatoForm(instance=fato)
    return render(request, 'registros/fato_form.html', {
        'form': form, 'titulo': f'Editar — {fato.titulo}', 'fato': fato,
    })


@login_required
def fato_excluir(request, pk):
    fato = get_object_or_404(Fato, pk=pk)
    if request.method == 'POST':
        titulo = fato.titulo
        fato.delete()
        messages.success(request, f'"{titulo}" excluído com sucesso.')
        return redirect('registros:fato_lista')
    return render(request, 'registros/fato_confirmar_exclusao.html', {'fato': fato})


# ══════════════════════════════════════════════
# RELATÓRIOS
# ══════════════════════════════════════════════

@login_required
def relatorio_lista(request):
    query = request.GET.get('q', '')
    relatorios = Relatorio.objects.all().order_by('-criado_em')
    if query:
        relatorios = relatorios.filter(titulo__icontains=query)
    return render(request, 'registros/relatorio_lista.html', {
        'relatorios': relatorios, 'query': query,
    })


@login_required
def relatorio_detalhe(request, pk):
    relatorio = get_object_or_404(Relatorio, pk=pk)
    return render(request, 'registros/relatorio_detalhe.html', {'relatorio': relatorio})


@login_required
def relatorio_criar(request):
    if request.method == 'POST':
        form = RelatorioForm(request.POST)
        if form.is_valid():
            relatorio = form.save(commit=False)
            relatorio.criado_por = request.user
            relatorio.save()
            form.save_m2m()
            messages.success(request, 'Relatório criado com sucesso!')
            return redirect('registros:relatorio_lista')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = RelatorioForm()
    return render(request, 'registros/relatorio_form.html', {
        'form': form, 'titulo': 'Novo Relatório',
    })


@login_required
def relatorio_editar(request, pk):
    relatorio = get_object_or_404(Relatorio, pk=pk)
    if request.method == 'POST':
        form = RelatorioForm(request.POST, instance=relatorio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Relatório atualizado com sucesso!')
            return redirect('registros:relatorio_detalhe', pk=relatorio.pk)
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = RelatorioForm(instance=relatorio)
    return render(request, 'registros/relatorio_form.html', {
        'form': form, 'titulo': f'Editar — {relatorio.titulo}', 'relatorio': relatorio,
    })


@login_required
def relatorio_excluir(request, pk):
    relatorio = get_object_or_404(Relatorio, pk=pk)
    if request.method == 'POST':
        titulo = relatorio.titulo
        relatorio.delete()
        messages.success(request, f'"{titulo}" excluído com sucesso.')
        return redirect('registros:relatorio_lista')
    return render(request, 'registros/relatorio_confirmar_exclusao.html', {'relatorio': relatorio})


# ══════════════════════════════════════════════
# MEMÓRIAS
# ══════════════════════════════════════════════

@login_required
def memoria_lista(request):
    query = request.GET.get('q', '')
    memorias = Memoria.objects.all().order_by('-fixada', '-criado_em')
    if query:
        memorias = memorias.filter(titulo__icontains=query)
    return render(request, 'registros/memoria_lista.html', {
        'memorias': memorias, 'query': query,
    })


@login_required
def memoria_detalhe(request, pk):
    memoria = get_object_or_404(Memoria, pk=pk)
    return render(request, 'registros/memoria_detalhe.html', {'memoria': memoria})


@login_required
def memoria_criar(request):
    if request.method == 'POST':
        form = MemoriaForm(request.POST)
        if form.is_valid():
            memoria = form.save(commit=False)
            memoria.criado_por = request.user
            memoria.save()
            form.save_m2m()
            messages.success(request, 'Memória registrada com sucesso!')
            return redirect('registros:memoria_lista')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = MemoriaForm()
    return render(request, 'registros/memoria_form.html', {
        'form': form, 'titulo': 'Nova Memória',
    })


@login_required
def memoria_editar(request, pk):
    memoria = get_object_or_404(Memoria, pk=pk)
    if request.method == 'POST':
        form = MemoriaForm(request.POST, instance=memoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Memória atualizada com sucesso!')
            return redirect('registros:memoria_detalhe', pk=memoria.pk)
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = MemoriaForm(instance=memoria)
    return render(request, 'registros/memoria_form.html', {
        'form': form, 'titulo': f'Editar — {memoria.titulo}', 'memoria': memoria,
    })


@login_required
def memoria_excluir(request, pk):
    memoria = get_object_or_404(Memoria, pk=pk)
    if request.method == 'POST':
        titulo = memoria.titulo
        memoria.delete()
        messages.success(request, f'"{titulo}" excluída com sucesso.')
        return redirect('registros:memoria_lista')
    return render(request, 'registros/memoria_confirmar_exclusao.html', {'memoria': memoria})