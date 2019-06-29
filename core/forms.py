from django.forms import ModelForm
from .models import Tipo, Doc

class TipoForm(ModelForm):
	class Meta():
		model = Tipo
		fields = ['nome']
		
class DocForm(ModelForm):
	class Meta():
		model = Doc
		fields = ['nome','arquivo', 'data', 'local']






