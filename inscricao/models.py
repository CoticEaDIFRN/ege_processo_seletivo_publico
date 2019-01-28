from django.db import models
from django.db.models import OneToOneField, CASCADE


class Candidato(models.Model):

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

    cpf = models.CharField('CPF', max_length=200, unique=True)
    nome_civil = models.CharField('Nome Civil', max_length=200)
    nome_social = models.CharField('Nome Social', max_length=200)
    nome_apresentacao = models.CharField('Nome de Apresentação', max_length=200)
    nome_usual = models.CharField('Nome Usual', max_length=200)
    data_nascimento = models.DateField('Data de Nascimento')
    estado_nascimento = models.CharField('Estado de Nascimento', max_length=200)
    nacionalidade = models.CharField('Nacionalidade', max_length=200)
    nome_mae = models.CharField('Nome da Mãe', max_length=200)
    nome_pai = models.CharField('Nome do Pai', max_length=200)
    sexo = models.PositiveIntegerField('Sexo', choices=SEXO)
    rg = models.PositiveIntegerField('RG')
    data_emissao = models.DateField('Data de emissão')
    estado_emissao = models.CharField('Estado Emissão', max_length=2, choices=ESTADO, default=RIOGRANDEDONORTE)
    telefone = models.CharField('Telefone', max_length=200)
    email = models.EmailField('E-mail', unique=True, null=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'cpf'
    is_anonymous = True
    is_authenticated = True

    def __str__(self):
        return self.nome_civil

class Endereco(models.Model):
    municipio = models.CharField('Município', max_length=200)
    pais_nascimento = models.CharField('País de Nascimento', max_length=200)
    cep = models.CharField('CEP', max_length=200)
    endereco = models.CharField('Endereço', max_length=200)
    complemento = models.CharField('Complento', max_length=200)
    uf = models.CharField('UF', max_length=200)
    cidade = models.CharField('Cidade', max_length=200)
    candidato = OneToOneField(
    Candidato,on_delete=CASCADE,
    )

    def __str__(self):
        return self.municipio


class Inscricao(models.Model):
    numero = models.CharField('Número', max_length=200)
    #processoSeletivo = models.ForeignKey(ProcessoSeletivo, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero