from django.db import models

class Tipo(models.Model):
	nome = models.CharField('Tipo', max_length=100)

class Doc(models.Model):
	nome = models.CharField('Nome', max_length=100)
	arquivo = models.FileField('Arquivo', upload_to='upload')
	data = models.DateTimeField('Data')
	local = models.CharField('Local Físico', max_length=100)


