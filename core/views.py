from django.shortcuts import render, redirect
from .models import Tipo
from .forms import TipoForm

def cadastro(request):
	return render(request, "cadastro.html")

def index(request):
	return render(request, "index.html")

def login(request):
	return render(request, "login.html")
	








