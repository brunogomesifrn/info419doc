from django.shortcuts import render, redirect
from .models import Tipo, Doc, cadastro
from .forms import TipoForm, DocForm, cadastroForm

#OUTRA COISA
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
	
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


#OUTRA COISA

def index(request):
	return render(request, "index.html")
@login_required
def perfil(request):
	return render(request, "perfil.html")


def registro(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	contexto = {
		'form': form
	}
	return render(request, 'registro.html', contexto)

@login_required
def dados(request, id):
	user = User.objects.get(pk=id)
	form = UserCreationForm(request.POST or None, instance=user)
	if form.is_valid():
		form.save()
		return redirect('perfil')
	contexto = {
		'form': form
	}
	return render(request, 'registro.html', contexto)