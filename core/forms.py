from django.forms import ModelForm
from .models import Tipo, Doc
from .models import cadastro, login, index

class TipoForm(ModelForm):
	class Meta():
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
