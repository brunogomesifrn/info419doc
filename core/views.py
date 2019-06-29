from django.shortcuts import render, redirect
from .models import Tipo, Doc
from .forms import TipoForm, DocForm

def cadastro(request):
	return render(request, "cadastro.html")

def index(request):
	return render(request, "index.html")

def login(request):
	return render(request, "login.html")
#@login_required
def perfil(request):
	return render(request, "perfil.html")
#CRUD DO TIPO
def tipo_cadastrar(request):
	form = TipoForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('tipo')
	contexto = {
		'form': form
	}
	return render(request, 'tipo_cadastro.html', contexto)


def tipo_listar(request):
	tipo = Tipo.objects.all()
	contexto = {
		'lista_tipo' : tipo
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
	return render(request, 'tipo_cadastro.html', contexto)

def tipo_deletar(request, id):
	tipo = Tipo.objects.get(pk=id)
	tipo.delete()
	return redirect('tipo')


#CRUD DOCUMENTO
def cadastroDoc(request):
	form = DocForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('doc')

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
		return redirect('doc')
	contexto = {
		'form': form
	}
	return render(request, 'cadastrar_documento.html', contexto)

def deletarDoc(request, id):
	doc = Doc.objects.get(pk=id)
	curso.delete()
	return redirect('doc')


