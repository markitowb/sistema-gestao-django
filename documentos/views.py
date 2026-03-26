import os
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Documento
from .forms import DocumentoForm


# ── Listagem ──────────────────────────────────────────────────
@login_required
def documento_lista(request):
    query = request.GET.get('q', '')
    tipo  = request.GET.get('tipo', '')
    documentos = Documento.objects.all().order_by('-criado_em')

    if query:
        documentos = documentos.filter(titulo__icontains=query)
    if tipo:
        documentos = documentos.filter(tipo=tipo)

    return render(request, 'documentos/lista.html', {
        'documentos': documentos,
        'query': query,
        'tipo': tipo,
        'tipo_choices': Documento.TIPO_CHOICES,
    })


# ── Detalhe ───────────────────────────────────────────────────
@login_required
def documento_detalhe(request, pk):
    documento = get_object_or_404(Documento, pk=pk)
    return render(request, 'documentos/detalhe.html', {'documento': documento})


# ── Cadastrar ─────────────────────────────────────────────────
@login_required
def documento_criar(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            documento = form.save(commit=False)
            documento.criado_por = request.user
            documento.save()
            form.save_m2m()
            messages.success(request, 'Documento cadastrado com sucesso!')
            return redirect('documentos:lista')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = DocumentoForm()
    return render(request, 'documentos/form.html', {
        'form': form, 'titulo': 'Cadastrar Documento',
    })


# ── Editar ────────────────────────────────────────────────────
@login_required
def documento_editar(request, pk):
    documento = get_object_or_404(Documento, pk=pk)
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES, instance=documento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Documento atualizado com sucesso!')
            return redirect('documentos:detalhe', pk=documento.pk)
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = DocumentoForm(instance=documento)
    return render(request, 'documentos/form.html', {
        'form': form,
        'titulo': f'Editar — {documento.titulo}',
        'documento': documento,
    })


# ── Excluir ───────────────────────────────────────────────────
@login_required
def documento_excluir(request, pk):
    documento = get_object_or_404(Documento, pk=pk)
    if request.method == 'POST':
        titulo = documento.titulo
        # Remove o arquivo físico do disco ao excluir
        if documento.arquivo and os.path.isfile(documento.arquivo.path):
            os.remove(documento.arquivo.path)
        documento.delete()
        messages.success(request, f'"{titulo}" excluído com sucesso.')
        return redirect('documentos:lista')
    return render(request, 'documentos/confirmar_exclusao.html', {'documento': documento})