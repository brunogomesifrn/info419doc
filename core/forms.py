from django.forms import ModelForm
from .models import Tipo, #Doc

class TipoForm(ModelForm):
	class Meta():
		model = Tipo
		fields = ['nome']
		
<<<<<<< HEAD
#class DocForm(ModelForm):
	#class Meta():
		#model = Doc
		#fields = ['nome', 'data', 'arquivo', 'local']
=======
class DocForm(ModelForm):
	class Meta():
		model = Doc
		fields = ['nome', 'data', 'arquivo', 'local']

class cadastroForm(ModelForm):
	class Meta:
		model = cadastro
		fields = ['usuario', 'senha', 'repetir_senha']
>>>>>>> fe4797f986f5325bb5214e9ba7b517170de79852
