from django.db import models

class Tipo(models.Model):
	nome = models.CharField('Tipo', max_length=100)

class Tipo_Cadastro(models.Model):
	nome = models.CharField('Tipo', max_length=100)

class Doc(models.Model):
	nome = models.CharField('Nome', max_length=100)
    data_inicio = models.DateField('Data de Início', null=True)
    arquivo = models.FileField('Arquivo', upload_to='upload')
    local = models.CharField('Local Físico' ax_length=100
