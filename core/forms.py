from django.forms import ModelForm
from .models import Tipo, Doc
from .models import cadastro

class TipoForm(ModelForm):
	class Meta():
<<<<<<< HEAD

=======
		model = cadastro
		fields = ['usuario', 'senha', 'repetir_senha']

class TipoForm(ModelForm):
	class Meta():
>>>>>>> fbf72fc478f680636269d4da81510285990091ad
		model = Tipo
		fields = ['nome']
		
class DocForm(ModelForm):
	class Meta():
		model = Doc
		fields = ['nome', 'data', 'arquivo', 'local']

<<<<<<< HEAD
		fields = ['nome', 'data_inicio', 'local']


		fields = ['nome', 'data', 'arquivo', 'local']
class cadastroForm(ModelForm):
	class Meta():
		model = cadastro
		fields = ['usuario', 'senha, repetir_senha']
=======
>>>>>>> fbf72fc478f680636269d4da81510285990091ad
