from django.db import models

class Tipo(models.Model):
	nome = models.CharField('Tipo', max_length=100)

class Doc(models.Model):
	nome = models.CharField('Nome', max_length=100)
    data_inicio = models.DateField('Data de Início', null=True)
    local = models.CharField('Local Físico')