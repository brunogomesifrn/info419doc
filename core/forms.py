from django.forms import ModelForm
from .models import Tipo, Doc
from .models import cadastro

class cadastroForm(ModelForm):
	class Meta():
<<<<<<< HEAD
=======
		model = cadastro
		fields = ['usuario', 'senha', 'repetir_senha']

class TipoForm(ModelForm):
	class Meta():
>>>>>>> 34089e8b0e6b16ec6275b47397990793c066bab6
		model = Tipo
		fields = ['nome']
		
class DocForm(ModelForm):
	class Meta():
		model = Doc
		fields = ['nome', 'data', 'arquivo', 'local']
<<<<<<< HEAD
=======

>>>>>>> 34089e8b0e6b16ec6275b47397990793c066bab6
