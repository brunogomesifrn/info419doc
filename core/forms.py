from django.forms import ModelForm
from .models import Tipo, Doc, cadastro, Cursos

class TipoForm(ModelForm):
	class Meta():
		model = Tipo
		fields = ['nome']
		
class DocForm(ModelForm):
	class Meta():
		model = Doc
		fields = ['nome','arquivo', 'data', 'local']

class cadastroForm(ModelForm):
	class Meta():
		model = cadastro
		fields = ['usuario', 'senha', 'repetir_senha']




