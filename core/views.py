from django.shortcuts import render, redirect
from .models import Tipo
from .forms import TipoForm

#CRUD DO TIPO


def CadastroTipo(request):
	form = TipoForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('tipo')

	contexto = {
		'form': form
	}
	return render(request, 'tipo.html', contexto)


def tipo(request):
	tipo = Tipo.objects.all()
	contexto = {
		'lista_tipo': tipo
	}
	return render(request, 'tipo.html', contexto)

def AtualizarTipo(request, id):
	tipo = Tipo.objects.get(pk=id)
	form = TipoForm(request.POST or None, request.FILES or None, instance=curso)
	if form.is_valid():
		form.save()
		return redirect('tipo')
	contexto = {
		'form': form
	}
	return render(request, 'cadastro.html', contexto)

def deletar(request, id):
	curso = Cursos.objects.get(pk=id)
	curso.delete()
	return redirect('cursos')


#CRUD DOCUMENTO



