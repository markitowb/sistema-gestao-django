from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib import colors
from reportlab.lib.units import cm

from .utils.pdf import gerar_pdf, estilos, campo, secao
from pessoas.models import Pessoa
from registros.models import Fato, Relatorio, Memoria


# ── PDF de Pessoa ─────────────────────────────────────────────
@login_required
def pdf_pessoa(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    sts = estilos()
    fl = []  # flowables

    fl.append(Paragraph(f'Ficha — {pessoa.nome_completo}', sts['titulo']))
    fl.append(Spacer(1, 0.3 * cm))

    # Dados pessoais
    fl += secao('Dados Pessoais', sts)
    dados = [
        [Paragraph('NOME COMPLETO', sts['label']),  Paragraph(pessoa.nome_completo or '—', sts['valor'])],
        [Paragraph('CPF',           sts['label']),  Paragraph(pessoa.cpf or '—', sts['valor'])],
        [Paragraph('RG',            sts['label']),  Paragraph(pessoa.rg or '—', sts['valor'])],
        [Paragraph('NASCIMENTO',    sts['label']),  Paragraph(pessoa.data_nascimento.strftime('%d/%m/%Y') if pessoa.data_nascimento else '—', sts['valor'])],
        [Paragraph('SEXO',          sts['label']),  Paragraph(pessoa.get_sexo_display(), sts['valor'])],
        [Paragraph('ESTADO CIVIL',  sts['label']),  Paragraph(pessoa.get_estado_civil_display() if pessoa.estado_civil else '—', sts['valor'])],
        [Paragraph('NACIONALIDADE', sts['label']),  Paragraph(pessoa.nacionalidade or '—', sts['valor'])],
        [Paragraph('NATURALIDADE',  sts['label']),  Paragraph(pessoa.naturalidade or '—', sts['valor'])],
    ]
    t = Table(dados, colWidths=[4 * cm, 13 * cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#eaf0fb')),
        ('ROWBACKGROUNDS', (1, 0), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')]),
        ('GRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#d5d8dc')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ]))
    fl.append(t)

    # Contato
    fl += secao('Contato', sts)
    contato = [
        [Paragraph('TELEFONE', sts['label']), Paragraph(pessoa.telefone or '—', sts['valor']),
         Paragraph('CELULAR',  sts['label']), Paragraph(pessoa.celular or '—', sts['valor'])],
        [Paragraph('E-MAIL',   sts['label']), Paragraph(pessoa.email or '—', sts['valor']),
         Paragraph('', sts['label']), Paragraph('', sts['valor'])],
    ]
    tc = Table(contato, colWidths=[3 * cm, 7.5 * cm, 3 * cm, 4 * cm])
    tc.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#eaf0fb')),
        ('BACKGROUND', (2, 0), (2, -1), colors.HexColor('#eaf0fb')),
        ('GRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#d5d8dc')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ]))
    fl.append(tc)

    # Endereço
    fl += secao('Endereço', sts)
    end = f'{pessoa.logradouro or "—"}, {pessoa.numero or "s/n"}'
    if pessoa.complemento:
        end += f', {pessoa.complemento}'
    end += f' — {pessoa.bairro or "—"}, {pessoa.cidade or "—"}/{pessoa.estado or "—"} — CEP: {pessoa.cep or "—"}'
    fl.append(Paragraph(end, sts['corpo']))

    # Vínculos
    if pessoa.empresas.exists() or pessoa.organizacoes.exists():
        fl += secao('Vínculos', sts)
        if pessoa.empresas.exists():
            fl.append(Paragraph('<b>Empresas:</b> ' + ', '.join(str(e) for e in pessoa.empresas.all()), sts['corpo']))
        if pessoa.organizacoes.exists():
            fl.append(Paragraph('<b>Organizações:</b> ' + ', '.join(str(o) for o in pessoa.organizacoes.all()), sts['corpo']))

    # Observações
    if pessoa.observacoes:
        fl += secao('Observações', sts)
        fl.append(Paragraph(pessoa.observacoes.replace('\n', '<br/>'), sts['corpo']))

    buffer = gerar_pdf(
        titulo=f'Ficha Pessoal — {pessoa.nome_completo}',
        conteudo_flowables=fl,
        usuario=request.user,
        tipo_sigilo='PESSOAL',
    )
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="pessoa_{pessoa.pk}.pdf"'
    return response


# ── PDF de Fato ───────────────────────────────────────────────
@login_required
def pdf_fato(request, pk):
    fato = get_object_or_404(Fato, pk=pk)
    sts = estilos()
    fl = []

    fl.append(Paragraph(fato.titulo, sts['titulo']))
    fl.append(Spacer(1, 0.3 * cm))

    fl += secao('Dados do Fato', sts)
    dados = [
        [Paragraph('TIPO',      sts['label']), Paragraph(fato.get_tipo_display(), sts['valor']),
         Paragraph('DATA/HORA', sts['label']), Paragraph(fato.data_fato.strftime('%d/%m/%Y %H:%M'), sts['valor'])],
        [Paragraph('LOCAL',     sts['label']), Paragraph(fato.local or '—', sts['valor']),
         Paragraph('FONTE',     sts['label']), Paragraph(fato.fonte or '—', sts['valor'])],
    ]
    t = Table(dados, colWidths=[3 * cm, 7.5 * cm, 3 * cm, 4 * cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#eaf0fb')),
        ('BACKGROUND', (2, 0), (2, -1), colors.HexColor('#eaf0fb')),
        ('GRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#d5d8dc')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ]))
    fl.append(t)

    fl += secao('Descrição', sts)
    fl.append(Paragraph(fato.descricao.replace('\n', '<br/>'), sts['corpo']))

    # Envolvidos
    if fato.pessoas.exists() or fato.empresas.exists() or fato.organizacoes.exists():
        fl += secao('Envolvidos', sts)
        if fato.pessoas.exists():
            fl.append(Paragraph('<b>Pessoas:</b> ' + ', '.join(str(p) for p in fato.pessoas.all()), sts['corpo']))
        if fato.empresas.exists():
            fl.append(Paragraph('<b>Empresas:</b> ' + ', '.join(str(e) for e in fato.empresas.all()), sts['corpo']))
        if fato.organizacoes.exists():
            fl.append(Paragraph('<b>Organizações:</b> ' + ', '.join(str(o) for o in fato.organizacoes.all()), sts['corpo']))

    # Documentos
    if fato.documentos.exists():
        fl += secao('Documentos Relacionados', sts)
        for doc in fato.documentos.all():
            fl.append(Paragraph(f'• {doc.titulo} ({doc.get_tipo_display()})', sts['corpo']))

    buffer = gerar_pdf(
        titulo=f'Fato — {fato.titulo}',
        conteudo_flowables=fl,
        usuario=request.user,
        tipo_sigilo='PREPARATORIO',
    )
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="fato_{fato.pk}.pdf"'
    return response


# ── PDF de Relatório ──────────────────────────────────────────
@login_required
def pdf_relatorio(request, pk):
    relatorio = get_object_or_404(Relatorio, pk=pk)
    sts = estilos()
    fl = []

    fl.append(Paragraph(relatorio.titulo, sts['titulo']))
    if relatorio.data_referencia:
        fl.append(Paragraph(
            f'Data de referência: {relatorio.data_referencia.strftime("%d/%m/%Y")}',
            sts['label']
        ))
    fl.append(Spacer(1, 0.4 * cm))

    fl += secao('Conteúdo', sts)
    for linha in relatorio.conteudo.split('\n'):
        if linha.strip():
            fl.append(Paragraph(linha, sts['corpo']))
        else:
            fl.append(Spacer(1, 0.2 * cm))

    # Envolvidos
    tem_envolvidos = (relatorio.pessoas.exists() or relatorio.empresas.exists() or
                      relatorio.organizacoes.exists())
    if tem_envolvidos:
        fl += secao('Envolvidos', sts)
        if relatorio.pessoas.exists():
            fl.append(Paragraph('<b>Pessoas:</b> ' + ', '.join(str(p) for p in relatorio.pessoas.all()), sts['corpo']))
        if relatorio.empresas.exists():
            fl.append(Paragraph('<b>Empresas:</b> ' + ', '.join(str(e) for e in relatorio.empresas.all()), sts['corpo']))
        if relatorio.organizacoes.exists():
            fl.append(Paragraph('<b>Organizações:</b> ' + ', '.join(str(o) for o in relatorio.organizacoes.all()), sts['corpo']))

    # Fatos relacionados
    if relatorio.fatos.exists():
        fl += secao('Fatos Relacionados', sts)
        for fato in relatorio.fatos.all():
            fl.append(Paragraph(
                f'• {fato.data_fato.strftime("%d/%m/%Y %H:%M")} — {fato.titulo}',
                sts['corpo']
            ))

    buffer = gerar_pdf(
        titulo=relatorio.titulo,
        conteudo_flowables=fl,
        usuario=request.user,
        tipo_sigilo='PREPARATORIO',
    )
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="relatorio_{relatorio.pk}.pdf"'
    return response


# ── PDF de Memória ────────────────────────────────────────────
@login_required
def pdf_memoria(request, pk):
    memoria = get_object_or_404(Memoria, pk=pk)
    sts = estilos()
    fl = []

    fl.append(Paragraph(memoria.titulo, sts['titulo']))
    if memoria.data_memoria:
        fl.append(Paragraph(
            f'Data: {memoria.data_memoria.strftime("%d/%m/%Y")}',
            sts['label']
        ))
    fl.append(Spacer(1, 0.4 * cm))

    fl += secao('Conteúdo', sts)
    for linha in memoria.conteudo.split('\n'):
        if linha.strip():
            fl.append(Paragraph(linha, sts['corpo']))
        else:
            fl.append(Spacer(1, 0.2 * cm))

    if memoria.pessoas.exists() or memoria.empresas.exists() or memoria.organizacoes.exists():
        fl += secao('Vínculos', sts)
        if memoria.pessoas.exists():
            fl.append(Paragraph('<b>Pessoas:</b> ' + ', '.join(str(p) for p in memoria.pessoas.all()), sts['corpo']))
        if memoria.empresas.exists():
            fl.append(Paragraph('<b>Empresas:</b> ' + ', '.join(str(e) for e in memoria.empresas.all()), sts['corpo']))
        if memoria.organizacoes.exists():
            fl.append(Paragraph('<b>Organizações:</b> ' + ', '.join(str(o) for o in memoria.organizacoes.all()), sts['corpo']))

    buffer = gerar_pdf(
        titulo=memoria.titulo,
        conteudo_flowables=fl,
        usuario=request.user,
        tipo_sigilo='PREPARATORIO',
    )
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="memoria_{memoria.pk}.pdf"'
    return response