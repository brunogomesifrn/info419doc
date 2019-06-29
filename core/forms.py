from django.forms import ModelForm
from .models import Tipo, Doc
from .models import cadastro, login, index

class TipoForm(ModelForm):
	class Meta():
<<<<<<< HEAD
=======
		model = Cursos
		fields = ['usuario', 'senha', 'repetir_senha']
>>>>>>> 8c5999e8254dd1e67391f509378bf6396498655a
		model = Tipo
		fields = ['nome']

class DocForm(ModelForm):
	class Meta():
		model = Doc
<<<<<<< HEAD
		fields = ['nome', 'data', 'arquivo', 'local']

=======
		fields = ['nome', 'data_inicio', 'local']
>>>>>>> 8c5999e8254dd1e67391f509378bf6396498655a
