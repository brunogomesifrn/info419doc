from django.forms import ModelForm
from .models import Tipo, Doc
from .models import cadastro

class cadastroForm(ModelForm):
	class Meta():

		model = cadastro
		fields = ['usuario', 'senha', 'repetir_senha']


		model = Cursos
		fields = ['usuario', 'senha', 'repetir_senha']

		model = Tipo
		fields = ['nome']

class DocForm(ModelForm):
	class Meta():
		model = Doc


		fields = ['nome', 'data', 'arquivo', 'local']

		fields = ['nome', 'data_inicio', 'local']


		fields = ['nome', 'data', 'arquivo', 'local']
