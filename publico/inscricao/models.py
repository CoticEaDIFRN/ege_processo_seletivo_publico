from django.db import models
#from cadastroEdital.models import Edital, Vaga


class ProcessoSeletivo(models.Model):
    edital = models.ForeignKey(Edital, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)

class Candidato(models.Model):
    SEXO = (
        (1, 'Feminino'),
        (2, 'Masculino'),
    )
    ESTADO = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espirito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('AC', 'Piauí'),
        ('RJ', 'RIo de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    nomeCivil = models.CharField('Nome Civil', max_length=200)
    nomeSocial = models.CharField('Nome Social', max_length=200)
    nomeApresentacao = models.CharField('Nome de Apresentação', max_length=200)
    nomeUsual = models.CharField('Nome Usual', max_length=200)
    data_nascimento = models.DateField()
    estado_nascimento = models.CharField('Estado de Nascimento', max_length=200)
    nacionalidade = models.CharField('Nacionalidade', max_length=200)
    nome_mae = models.CharField('Nome da Mãe', max_length=200)
    nome_pai = models.CharField('Nome do Pai', max_length=200)
    cpf = models.CharField('CPF', max_length=200)
    sexo = models.PositiveIntegerField('Sexo', choices=SEXO)
    rg = models.PositiveIntegerField('RG')
    data_emissao = models.DateField('Data de emissão')
    estado_emissao = models.PositiveIntegerField('Estado Emissão', choices=ESTADO)
    telefone = models.CharField('Telefone', max_length=200)
    email = models.CharField('E-mail', max_length=200)

    def __str__(self):
        return self.nomeCivil


class Endereco(models.Model):
    municipio = models.CharField('Município', max_length=200)
    pais_nascimento = models.CharField('País de Nascimento', max_length=200)
    cep = models.CharField('CEP', max_length=200)
    endereco = models.CharField('Endereço', max_length=200)
    complemento = models.CharField('Complento', max_length=200)
    uf = models.CharField('UF', max_length=200)
    cidade = models.CharField('Cidade', max_length=200)
    candidato = models.OneToOneField(
        Candidato,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.municipio


class Inscricao(models.Model):
    numero = models.CharField('Número', max_length=200)
    processoSeletivo = models.ForeignKey(ProcessoSeletivo, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero
