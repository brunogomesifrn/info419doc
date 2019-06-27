from django.db import models

class Tipo(models.Model):
	nome = models.CharField('Tipo', max_length=100)
