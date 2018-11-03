from django.db import models
from django.conf import settings

class Login(models.Model):
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class Fisioterapeuta(models.Model):
    nome = models.CharField(max_length=100)
    cpfFisioterapeuta = models.CharField(max_length=20)
    crefito = models.CharField(max_length=15)
    especialidade = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpfPaciente = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=40)
    cep = models.CharField(max_length=15)
    cidade = models.CharField(max_length=40)
    uf = models.CharField(max_length=2, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    dataNascimento = models.DateField()
    responsavel = models.CharField(max_length=100, blank=True, null=True)
    cpfResponsavel = models.CharField(max_length=20, blank=True, null=True)
    diagnostico = models.CharField(max_length=200)
    descricaoDiagnostico = models.TextField()
    fotos = models.ImageField(upload_to='paciente_fotos', blank=True, null=True)

    def __str__(self):
        return self.nome

class Anotacao_Paciente(models.Model):
    data = models.DateField()
    anotacao = models.TextField()
    parteCorpo = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.parteCorpo

class Dados_Musculos(models.Model):
    dadosMusculos = models.IntegerField()
    dia = models.DateTimeField()