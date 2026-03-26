from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from io import BytesIO
from django.utils import timezone

# ── Constantes de sigilo ──────────────────────────────────────
SIGILO = {
    'PESSOAL':      ('INFORMAÇÃO PESSOAL',                    colors.HexColor('#1a5276')),
    'RESERVADO':    ('RESERVADO',                             colors.HexColor('#7b241c')),
    'PREPARATORIO': ('DOCUMENTO PREPARATÓRIO — ACESSO RESTRITO', colors.HexColor('#784212')),
}

NOME_INSTITUICAO = 'Sistema de Gestão'  # ← altere para o nome da sua instituição
BASE_LEGAL_PESSOAL     = 'Informação Pessoal protegida nos termos do art. 31 da LAI (Lei nº 12.527/2011) e da LGPD (Lei nº 13.709/2018).'
BASE_LEGAL_PREPARATORIO = 'Documento Preparatório — Acesso Restrito nos termos do art. 7º, §3º da LAI (Lei nº 12.527/2011).'
BASE_LEGAL_RESERVADO    = 'Informação classificada como Reservada nos termos do art. 24 da LAI (Lei nº 12.527/2011).'


def _base_legal(tipo_sigilo):
    if tipo_sigilo == 'PESSOAL':
        return BASE_LEGAL_PESSOAL
    elif tipo_sigilo == 'PREPARATORIO':
        return BASE_LEGAL_PREPARATORIO
    return BASE_LEGAL_RESERVADO


def gerar_pdf(titulo, conteudo_flowables, usuario, tipo_sigilo='PREPARATORIO'):
    """
    Gera um PDF com cabeçalho, rodapé e carimbo de sigilo padronizados.

    Parâmetros:
      titulo           — título do documento (aparece no cabeçalho)
      conteudo_flowables — lista de Flowables do ReportLab (Paragraph, Table, Spacer...)
      usuario          — objeto User do Django (para o rodapé)
      tipo_sigilo      — 'PESSOAL', 'RESERVADO' ou 'PREPARATORIO'

    Retorna:
      BytesIO com o PDF gerado (pronto para HttpResponse)
    """
    buffer = BytesIO()
    largura, altura = A4
    margem = 2 * cm

    label_sigilo, cor_sigilo = SIGILO[tipo_sigilo]
    base_legal = _base_legal(tipo_sigilo)
    agora = timezone.localtime(timezone.now()).strftime('%d/%m/%Y às %H:%M')
    nome_usuario = usuario.get_full_name() or usuario.username

    def cabecalho_rodape(canvas, doc):
        canvas.saveState()

        # ── Faixa de sigilo no TOPO ───────────────────────────
        canvas.setFillColor(cor_sigilo)
        canvas.rect(0, altura - 1.2 * cm, largura, 1.2 * cm, fill=1, stroke=0)
        canvas.setFillColor(colors.white)
        canvas.setFont('Helvetica-Bold', 9)
        canvas.drawCentredString(largura / 2, altura - 0.8 * cm, label_sigilo)

        # ── Cabeçalho principal ───────────────────────────────
        canvas.setFillColor(colors.HexColor('#2c3e50'))
        canvas.rect(0, altura - 3.0 * cm, largura, 1.8 * cm, fill=1, stroke=0)

        canvas.setFillColor(colors.white)
        canvas.setFont('Helvetica-Bold', 13)
        canvas.drawString(margem, altura - 1.9 * cm, NOME_INSTITUICAO)

        canvas.setFont('Helvetica', 9)
        canvas.drawRightString(largura - margem, altura - 1.9 * cm, titulo)
        canvas.drawString(margem, altura - 2.6 * cm, f'Gerado em: {agora}')
        canvas.drawRightString(largura - margem, altura - 2.6 * cm, f'Usuário: {nome_usuario}')

        # ── Linha separadora ──────────────────────────────────
        canvas.setStrokeColor(colors.HexColor('#2c3e50'))
        canvas.setLineWidth(0.5)
        canvas.line(margem, altura - 3.1 * cm, largura - margem, altura - 3.1 * cm)

        # ── Rodapé ────────────────────────────────────────────
        canvas.setFillColor(colors.HexColor('#f2f3f4'))
        canvas.rect(0, 0, largura, 1.8 * cm, fill=1, stroke=0)

        canvas.setFillColor(colors.HexColor('#5d6d7e'))
        canvas.setFont('Helvetica', 7)
        canvas.drawString(margem, 1.2 * cm, base_legal)
        canvas.drawString(margem, 0.7 * cm, f'Documento gerado em {agora} por {nome_usuario}')
        canvas.drawRightString(largura - margem, 0.7 * cm,
                               f'Página {doc.page}')

        # ── Faixa de sigilo no RODAPÉ ─────────────────────────
        canvas.setFillColor(cor_sigilo)
        canvas.rect(0, 0, largura, 0.5 * cm, fill=1, stroke=0)
        canvas.setFillColor(colors.white)
        canvas.setFont('Helvetica-Bold', 7)
        canvas.drawCentredString(largura / 2, 0.15 * cm, label_sigilo)

        canvas.restoreState()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        topMargin=3.5 * cm,
        bottomMargin=2.2 * cm,
        leftMargin=margem,
        rightMargin=margem,
    )
    doc.build(conteudo_flowables, onFirstPage=cabecalho_rodape, onLaterPages=cabecalho_rodape)
    buffer.seek(0)
    return buffer


# ── Estilos reutilizáveis ─────────────────────────────────────
def estilos():
    base = getSampleStyleSheet()
    return {
        'titulo':    ParagraphStyle('titulo',    fontSize=16, fontName='Helvetica-Bold',
                                    spaceAfter=6, textColor=colors.HexColor('#2c3e50')),
        'subtitulo': ParagraphStyle('subtitulo', fontSize=12, fontName='Helvetica-Bold',
                                    spaceAfter=4, spaceBefore=12, textColor=colors.HexColor('#2c3e50')),
        'label':     ParagraphStyle('label',     fontSize=9,  fontName='Helvetica-Bold',
                                    textColor=colors.HexColor('#5d6d7e')),
        'valor':     ParagraphStyle('valor',     fontSize=10, fontName='Helvetica',
                                    spaceAfter=4),
        'corpo':     ParagraphStyle('corpo',     fontSize=10, fontName='Helvetica',
                                    leading=14, spaceAfter=6, alignment=TA_JUSTIFY),
        'rodape_aviso': ParagraphStyle('rodape_aviso', fontSize=8, fontName='Helvetica-Oblique',
                                       textColor=colors.HexColor('#7f8c8d'), alignment=TA_CENTER),
    }


def campo(label, valor, sts):
    """Retorna um bloco label + valor formatado."""
    itens = [Paragraph(label.upper(), sts['label'])]
    itens.append(Paragraph(str(valor) if valor else '—', sts['valor']))
    return itens


def secao(titulo, sts):
    """Retorna um título de seção com linha separadora."""
    return [
        Spacer(1, 0.3 * cm),
        Paragraph(titulo, sts['subtitulo']),
        HRFlowable(width='100%', thickness=0.5, color=colors.HexColor('#2c3e50')),
        Spacer(1, 0.2 * cm),
    ]

