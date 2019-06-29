from django.forms import ModelForm
from .models import Tipo, Doc
from .models import cadastro

class cadastroForm(ModelForm):
	class Meta():
<<<<<<< HEAD
=======

		model = cadastro
		fields = ['usuario', 'senha', 'repetir_senha']


>>>>>>> 8092c1ecaab74a4b1b80a91626a62c6d23629a2c
		model = Cursos
		fields = ['usuario', 'senha', 'repetir_senha']

		model = Tipo
		fields = ['nome']

class TipoForm(ModelForm):
	class Meta():
		model = Tipo
		fields = ['nome']
		
class DocForm(ModelForm):
	class Meta():
		model = Doc


		fields = ['nome', 'data', 'arquivo', 'local']

		fields = ['nome', 'data_inicio', 'local']


		fields = ['nome', 'data', 'arquivo', 'local']
