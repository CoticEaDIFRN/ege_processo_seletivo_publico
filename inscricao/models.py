from django.db import models
from django.db.models import Model, ForeignKey, OneToOneField, CASCADE
from django.db.models import CharField, BooleanField, URLField, PositiveIntegerField, DateTimeField, DateField, DecimalField, FloatField, EmailField


class Candidato(Model):

    SEXO = (
        (1, 'Feminino'),
        (2, 'Masculino'),
    )

    ACRE = 'AC'
    ALAGOAS = 'AL'
    AMAPA = 'AP'
    AMAZONAS = 'AM'
    BAHIA = 'BA'
    CEARÁ = 'CE'
    DISTRITOFEDERAL = 'DF'
    ESPIRITOSANTO = 'ES'
    GOIAS = 'GO'
    MARANHAO = 'MA'
    MATOGROSSO = 'MT'
    MATOGROSSOSUL = 'MS'
    MINASGERAIS = 'MG'
    PARA = 'PA'
    PARAIBA = 'PB'
    PARANA = 'PR'
    PERNAMBUCO = 'PE'
    PIAUI = 'PI'
    RIODEJANEIRO = 'RJ'
    RIOGRANDEDONORTE = 'RN'
    RIOGRANDEDOSUL = 'RS'
    RONDONIA = 'RO'
    RORAIMA = 'RR'
    SANTACATARINA = 'SC'
    SAOPAULO = 'SP'
    SERGIPE = 'SE'
    TOCANTINS = 'TO'

    ESTADO = (
        (ACRE, 'Acre'),
        (ALAGOAS, 'Alagoas'),
        (AMAPA, 'Amapá'),
        (AMAZONAS, 'Amazonas'),
        (BAHIA, 'Bahia'),
        (CEARÁ, 'Ceará'),
        (DISTRITOFEDERAL, 'Distrito Federal'),
        (ESPIRITOSANTO, 'Espirito Santo'),
        (GOIAS, 'Goiás'),
        (MARANHAO, 'Maranhão'),
        (MATOGROSSO, 'Mato Grosso'),
        (MATOGROSSOSUL, 'Mato Grosso do Sul'),
        (MINASGERAIS, 'Minas Gerais'),
        (PARA, 'Pará'),
        (PARAIBA, 'Paraíba'),
        (PARANA, 'Paraná'),
        (PERNAMBUCO, 'Pernambuco'),
        (PIAUI, 'Piauí'),
        (RIODEJANEIRO, 'Rio de Janeiro'),
        (RIOGRANDEDONORTE, 'Rio Grande do Norte'),
        (RIOGRANDEDOSUL, 'Rio Grande do Sul'),
        (RONDONIA, 'Rondônia'),
        (RORAIMA, 'Roraima'),
        (SANTACATARINA, 'Santa Catarina'),
        (SAOPAULO, 'São Paulo'),
        (SERGIPE, 'Sergipe'),
        (TOCANTINS, 'Tocantins'),
    )

    cpf = CharField('CPF', max_length=150, unique=True)
    nome_civil = CharField('Nome Civil', max_length=150)
    nome_social = CharField('Nome Social', max_length=150)
    nome_apresentacao = CharField('Nome de Apresentação', max_length=150)
    nome_usual = CharField('Nome Usual', max_length=150)
    data_nascimento = DateField('Data de Nascimento')
    nome_mae = CharField('Nome da Mãe', max_length=150)
    nome_pai = CharField('Nome do Pai', max_length=150)
    sexo = PositiveIntegerField('Sexo', choices=SEXO)
    rg = PositiveIntegerField('RG')
    data_emissao = DateField('Data de emissão')
    estado_emissao = CharField('Estado Emissão', max_length=2, choices=ESTADO, default=RIOGRANDEDONORTE)
    orgao_rg = CharField('Órgão do RG', max_length=100)
    telefone = CharField('Telefone', max_length=150)
    email = EmailField('E-mail', unique=True)
    pais_nascimento = CharField('País de Nascimento', max_length=100)
    estado_nascimento = CharField('Estado de Nascimento', max_length=2, choices=ESTADO, default=RIOGRANDEDONORTE)
    cidade_nascimento = CharField('Município de Nascimento', max_length=150)
    cep = CharField('CEP', max_length=50)
    endereco = CharField('Endereço', max_length=200)
    complemento = CharField('Complento', max_length=100, null=True)
    uf = CharField('UF', max_length=100)
    cidade = CharField('Cidade', max_length=100)


    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'cpf'
    is_anonymous = True
    is_authenticated = True

    def __str__(self):
        return self.cpf


#class Inscricao(Model):
#    numero = models.CharField('Número', max_length=200)
#    #processoSeletivo = models.ForeignKey(ProcessoSeletivo, on_delete=models.CASCADE)
#    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.numero

