from django.db import models

# Criado os models aqui.

class Pessoa(models.Model):

    # ── Choices ──────────────────────────────────────────────
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
        ('N', 'Não informado'),
    ]

    ESTADO_CIVIL_CHOICES = [
        ('SO', 'Solteiro(a)'),
        ('CA', 'Casado(a)'),
        ('DI', 'Divorciado(a)'),
        ('VI', 'Viúvo(a)'),
        ('UE', 'União Estável'),
    ]

    # ── Dados pessoais ────────────────────────────────────────
    nome_completo  = models.CharField('Nome completo', max_length=300)
    cpf            = models.CharField('CPF', max_length=14, unique=True, blank=True, null=True)
    rg             = models.CharField('RG', max_length=20, blank=True)
    data_nascimento = models.DateField('Data de nascimento', blank=True, null=True)
    sexo           = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES, default='N')
    estado_civil   = models.CharField('Estado civil', max_length=2, choices=ESTADO_CIVIL_CHOICES, blank=True)
    nacionalidade  = models.CharField('Nacionalidade', max_length=100, blank=True, default='Brasileira')
    naturalidade   = models.CharField('Naturalidade', max_length=100, blank=True)
    foto           = models.ImageField('Foto', upload_to='pessoas/fotos/', blank=True, null=True)

    # ── Contato ───────────────────────────────────────────────
    telefone       = models.CharField('Telefone', max_length=20, blank=True)
    celular        = models.CharField('Celular', max_length=20, blank=True)
    email          = models.EmailField('E-mail', blank=True)

    # ── Endereço ──────────────────────────────────────────────
    logradouro     = models.CharField('Logradouro', max_length=300, blank=True)
    numero         = models.CharField('Número', max_length=10, blank=True)
    complemento    = models.CharField('Complemento', max_length=100, blank=True)
    bairro         = models.CharField('Bairro', max_length=100, blank=True)
    cidade         = models.CharField('Cidade', max_length=100, blank=True)
    estado         = models.CharField('Estado (UF)', max_length=2, blank=True)
    cep            = models.CharField('CEP', max_length=9, blank=True)

    # ── Relacionamentos ───────────────────────────────────────
    empresas       = models.ManyToManyField(
        'Empresa',
        blank=True,
        related_name='pessoas',
        verbose_name='Empresas vinculadas'
    )
    organizacoes   = models.ManyToManyField(
        'Organizacao',
        blank=True,
        related_name='pessoas',
        verbose_name='Organizações vinculadas'
    )

    # ── Observações ───────────────────────────────────────────
    observacoes    = models.TextField('Observações', blank=True)

    # ── Controle interno ──────────────────────────────────────
    criado_em      = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em  = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['nome_completo']

    def __str__(self):
        return self.nome_completo
    
class Empresa(models.Model):

    # ── Choices ──────────────────────────────────────────────
    PORTE_CHOICES = [
        ('ME', 'Microempresa'),
        ('PE', 'Pequeno porte'),
        ('MD', 'Médio porte'),
        ('GR', 'Grande porte'),
    ]

    SITUACAO_CHOICES = [
        ('AT', 'Ativa'),
        ('IN', 'Inativa'),
        ('SU', 'Suspensa'),
        ('EX', 'Extinta'),
    ]

    # ── Dados principais ──────────────────────────────────────
    razao_social   = models.CharField('Razão social', max_length=300)
    nome_fantasia  = models.CharField('Nome fantasia', max_length=300, blank=True)
    cnpj           = models.CharField('CNPJ', max_length=18, unique=True, blank=True, null=True)
    inscricao_estadual = models.CharField('Inscrição estadual', max_length=30, blank=True)
    porte          = models.CharField('Porte', max_length=2, choices=PORTE_CHOICES, blank=True)
    situacao       = models.CharField('Situação', max_length=2, choices=SITUACAO_CHOICES, default='AT')
    ramo_atividade = models.CharField('Ramo de atividade', max_length=200, blank=True)
    data_fundacao  = models.DateField('Data de fundação', blank=True, null=True)
    logo           = models.ImageField('Logo', upload_to='empresas/logos/', blank=True, null=True)

    # ── Contato ───────────────────────────────────────────────
    telefone       = models.CharField('Telefone', max_length=20, blank=True)
    email          = models.EmailField('E-mail', blank=True)
    site           = models.URLField('Site', blank=True)

    # ── Endereço ──────────────────────────────────────────────
    logradouro     = models.CharField('Logradouro', max_length=300, blank=True)
    numero         = models.CharField('Número', max_length=10, blank=True)
    complemento    = models.CharField('Complemento', max_length=100, blank=True)
    bairro         = models.CharField('Bairro', max_length=100, blank=True)
    cidade         = models.CharField('Cidade', max_length=100, blank=True)
    estado         = models.CharField('Estado (UF)', max_length=2, blank=True)
    cep            = models.CharField('CEP', max_length=9, blank=True)

    # ── Observações ───────────────────────────────────────────
    observacoes    = models.TextField('Observações', blank=True)

    # ── Controle interno ──────────────────────────────────────
    criado_em      = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em  = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['razao_social']

    def __str__(self):
        return self.nome_fantasia or self.razao_social


# ─────────────────────────────────────────────────────────────


class Organizacao(models.Model):

    # ── Choices ──────────────────────────────────────────────
    TIPO_CHOICES = [
        ('ONG',  'ONG'),
        ('GOV',  'Órgão governamental'),
        ('MIL',  'Militar / policial'),
        ('INT',  'Internacional'),
        ('ASS',  'Associação'),
        ('SIN',  'Sindicato'),
        ('PAR',  'Partido político'),
        ('OUT',  'Outro'),
    ]

    SITUACAO_CHOICES = [
        ('AT', 'Ativa'),
        ('IN', 'Inativa'),
        ('EX', 'Extinta'),
    ]

    # ── Dados principais ──────────────────────────────────────
    nome           = models.CharField('Nome', max_length=300)
    sigla          = models.CharField('Sigla', max_length=30, blank=True)
    tipo           = models.CharField('Tipo', max_length=3, choices=TIPO_CHOICES, blank=True)
    situacao       = models.CharField('Situação', max_length=2, choices=SITUACAO_CHOICES, default='AT')
    area_atuacao   = models.CharField('Área de atuação', max_length=200, blank=True)
    data_fundacao  = models.DateField('Data de fundação', blank=True, null=True)
    logo           = models.ImageField('Logo', upload_to='organizacoes/logos/', blank=True, null=True)

    # ── Vinculações entre organizações ───────────────────────
    organizacoes_vinculadas = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=True,
        verbose_name='Organizações vinculadas'
    )

    # ── Contato ───────────────────────────────────────────────
    telefone       = models.CharField('Telefone', max_length=20, blank=True)
    email          = models.EmailField('E-mail', blank=True)
    site           = models.URLField('Site', blank=True)

    # ── Endereço ──────────────────────────────────────────────
    logradouro     = models.CharField('Logradouro', max_length=300, blank=True)
    numero         = models.CharField('Número', max_length=10, blank=True)
    complemento    = models.CharField('Complemento', max_length=100, blank=True)
    bairro         = models.CharField('Bairro', max_length=100, blank=True)
    cidade         = models.CharField('Cidade', max_length=100, blank=True)
    estado         = models.CharField('Estado (UF)', max_length=2, blank=True)
    cep            = models.CharField('CEP', max_length=9, blank=True)

    # ── Observações ───────────────────────────────────────────
    observacoes    = models.TextField('Observações', blank=True)

    # ── Controle interno ──────────────────────────────────────
    criado_em      = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em  = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Organização'
        verbose_name_plural = 'Organizações'
        ordering = ['nome']

    def __str__(self):
        return f'{self.sigla} – {self.nome}' if self.sigla else self.nome
    