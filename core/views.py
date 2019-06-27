from django.shortcuts import render, redirect
from .models import Tipo
from .forms import TipoForm


#CRUD DO TIPO


def tipo_cadastro(request):
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

def tipo_atualizar(request, id):
	tipo = Tipo.objects.get(pk=id)
	form = TipoForm(request.POST or None, request.FILES or None, instance=curso)
	if form.is_valid():
		form.save()
		return redirect('tipo')
	contexto = {
		'form': form
	}
	return render(request, 'cadastro.html', contexto)

def tipo_deletar(request, id):
	tipo = Tipo.objects.get(pk=id)
	tipo.delete()
	return redirect('tipo')


#CRUD DOCUMENTO
def cadastroDoc(request):
	form = DocForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('documento')

	contexto = {
		'form': form
	}
	return render(request, 'documento.html', contexto)


def documento(request):
	doc = Doc.objects.all()
	contexto = {
		'lista_doc': doc
	}
	return render(request, 'documento.html', contexto)

def atualizarDoc(request, id):
	doc = Doc.objects.get(pk=id)
	form = DocForm(request.POST or None, request.FILES or None, instance=curso)
	if form.is_valid():
		form.save()
		return redirect('documento')
	contexto = {
		'form': form
	}
	return render(request, 'cadastro.html', contexto)

def deletarDoc(request, id):
	doc = Doc.objects.get(pk=id)
	curso.delete()
	return redirect('documento')


