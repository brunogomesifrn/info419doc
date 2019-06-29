from django.forms import ModelForm
from .models import Tipo, Doc
from .models import cadastro

class cadastroForm(ModelForm):
	class Meta():
		model = cadastro
		fields = ['usuario', 'senha', 'repetir_senha']

class TipoForm(ModelForm):
	class Meta():
		model = Tipo
		fields = ['nome']
		
class DocForm(ModelForm):
	class Meta():
		model = Doc
		fields = ['nome', 'data', 'arquivo', 'local']

