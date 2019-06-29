from django.forms import ModelForm
from .models import Tipo, Doc

class TipoForm(ModelForm):
	class Meta():
<<<<<<< HEAD
		model = Cursos
		fields = ['usuario', 'senha', 'repetir_senha']
=======
		model = Tipo
		fields = ['nome']



class DocForm(ModelForm):
	class Meta():
		model = Doc
		fields = ['nome', 'data_inicio', 'local']
>>>>>>> 6b34178ff8d05853bb19bacd45977e68b18b41b9
