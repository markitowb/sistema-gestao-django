from django.db import models
from pessoas.models import Pessoa, Empresa, Organizacao
from documentos.models import Documento

# Create your models here.


class Fato(models.Model):

    TIPO_CHOICES = [
        ('OBS', 'Observação'),
        ('EVE', 'Evento'),
        ('INC', 'Incidente'),
        ('RES', 'Reunião'),
        ('OUT', 'Outro'),
    ]

    # ── Dados principais ──────────────────────────────────────
    titulo      = models.CharField('Título', max_length=300)
    tipo        = models.CharField('Tipo', max_length=3, choices=TIPO_CHOICES, default='OBS')
    descricao   = models.TextField('Descrição')
    data_fato   = models.DateTimeField('Data/hora do fato')
    local       = models.CharField('Local', max_length=300, blank=True)
    fonte       = models.CharField('Fonte', max_length=300, blank=True)
    confidencial = models.BooleanField('Confidencial', default=False)

    # ── Relacionamentos ───────────────────────────────────────
    pessoas     = models.ManyToManyField(
        Pessoa,
        blank=True,
        related_name='fatos',
        verbose_name='Pessoas envolvidas'
    )
    empresas    = models.ManyToManyField(
        Empresa,
        blank=True,
        related_name='fatos',
        verbose_name='Empresas envolvidas'
    )
    organizacoes = models.ManyToManyField(
        Organizacao,
        blank=True,
        related_name='fatos',
        verbose_name='Organizações envolvidas'
    )
    documentos  = models.ManyToManyField(
        Documento,
        blank=True,
        related_name='fatos',
        verbose_name='Documentos relacionados'
    )

    # ── Controle interno ──────────────────────────────────────
    criado_por  = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='fatos_criados',
        verbose_name='Criado por'
    )
    criado_em   = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Fato'
        verbose_name_plural = 'Fatos'
        ordering = ['-data_fato']

    def __str__(self):
        return f'{self.data_fato:%d/%m/%Y} — {self.titulo}'


# ─────────────────────────────────────────────────────────────


class Relatorio(models.Model):

    # ── Dados principais ──────────────────────────────────────
    titulo      = models.CharField('Título', max_length=300)
    conteudo    = models.TextField('Conteúdo')
    data_referencia = models.DateField('Data de referência', blank=True, null=True)

    # ── Relacionamentos ───────────────────────────────────────
    pessoas     = models.ManyToManyField(Pessoa,      blank=True, related_name='relatorios')
    empresas    = models.ManyToManyField(Empresa,     blank=True, related_name='relatorios')
    organizacoes = models.ManyToManyField(Organizacao, blank=True, related_name='relatorios')
    fatos       = models.ManyToManyField(Fato,        blank=True, related_name='relatorios')
    documentos  = models.ManyToManyField(Documento,   blank=True, related_name='relatorios')

    # ── Controle interno ──────────────────────────────────────
    criado_por  = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='relatorios_criados',
        verbose_name='Criado por'
    )
    criado_em   = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Relatório'
        verbose_name_plural = 'Relatórios'
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo


# ─────────────────────────────────────────────────────────────


class Memoria(models.Model):

    # ── Dados principais ──────────────────────────────────────
    titulo      = models.CharField('Título', max_length=300)
    conteudo    = models.TextField('Conteúdo')
    data_memoria = models.DateField('Data', blank=True, null=True)
    fixada      = models.BooleanField('Fixada', default=False)

    # ── Relacionamentos ───────────────────────────────────────
    pessoas     = models.ManyToManyField(Pessoa,      blank=True, related_name='memorias')
    empresas    = models.ManyToManyField(Empresa,     blank=True, related_name='memorias')
    organizacoes = models.ManyToManyField(Organizacao, blank=True, related_name='memorias')

    # ── Controle interno ──────────────────────────────────────
    criado_por  = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='memorias_criadas',
        verbose_name='Criado por'
    )
    criado_em   = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Memória'
        verbose_name_plural = 'Memórias'
        ordering = ['-fixada', '-criado_em']

    def __str__(self):
        return self.titulo
    