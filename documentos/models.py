from django.db import models
from pessoas.models import Pessoa, Empresa, Organizacao

# Create your models here.

class Documento(models.Model):

    # ── Choices ──────────────────────────────────────────────
    TIPO_CHOICES = [
        ('PDF',   'PDF'),
        ('WORD',  'Word (.docx)'),
        ('EXCEL', 'Excel (.xlsx)'),
        ('ODT',   'LibreOffice (.odt)'),
        ('IMG',   'Imagem'),
        ('OUT',   'Outro'),
    ]

    CATEGORIA_CHOICES = [
        ('REL', 'Relatório'),
        ('LAU', 'Laudo'),
        ('OFF', 'Ofício'),
        ('CON', 'Contrato'),
        ('ID',  'Documento de identificação'),
        ('FIN', 'Financeiro'),
        ('JUD', 'Judicial'),
        ('OUT', 'Outro'),
    ]

    # ── Dados principais ──────────────────────────────────────
    titulo      = models.CharField('Título', max_length=300)
    tipo        = models.CharField('Tipo', max_length=5, choices=TIPO_CHOICES)
    categoria   = models.CharField('Categoria', max_length=3, choices=CATEGORIA_CHOICES, blank=True)
    descricao   = models.TextField('Descrição', blank=True)
    arquivo     = models.FileField('Arquivo', upload_to='documentos/%Y/%m/')
    data_documento = models.DateField('Data do documento', blank=True, null=True)

    # ── Relacionamentos ───────────────────────────────────────
    pessoas     = models.ManyToManyField(
        Pessoa,
        blank=True,
        related_name='documentos',
        verbose_name='Pessoas relacionadas'
    )
    empresas    = models.ManyToManyField(
        Empresa,
        blank=True,
        related_name='documentos',
        verbose_name='Empresas relacionadas'
    )
    organizacoes = models.ManyToManyField(
        Organizacao,
        blank=True,
        related_name='documentos',
        verbose_name='Organizações relacionadas'
    )

    # ── Controle interno ──────────────────────────────────────
    criado_por  = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='documentos_criados',
        verbose_name='Criado por'
    )
    criado_em   = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering = ['-data_documento']

    def __str__(self):
        return self.titulo