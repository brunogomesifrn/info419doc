"""info419doc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import tipo_listar, tipo_cadastrar, tipo_atualizar, tipo_deletar
<<<<<<< HEAD
from core.views import documento doc_cadastrar, doc_atualizar, doc_deletar
from core.views import cadastro, index, login

=======
from core.views import documento, cadastrarDoc, atualizarDoc, deletarDoc
from core.views import doc_lista, doc_cadastrar, doc_atualizar, doc_deletar
from core.views import cadastro, index, login


>>>>>>> 34089e8b0e6b16ec6275b47397990793c066bab6

urlpatterns = [
	#URLs de Tipo
	path('tipo/', tipo_listar, name='tipo'),
	path('tipo_cadastrar/', tipo_cadastrar, name='tipo_cadastrar'),
	path('tipo_atualizar/<int:id>/', tipo_atualizar, name='tipo_atualizar'),
	path('tpo_deletar/<int:id>/', tipo_deletar, name='tipo_deletar'),

    #URLs de Perfi
    path('perfil/', perfil, name='perfi'),



    #URLs de documento
    path('documento/', documento, name='doc'),
    path('cadastrarDoc/', cadastrarDoc, name='cadastrarDoc'),
    path('atualizarDoc/<int:id>/', atualizarDoc, name='atualizarDoc'),
    path('deletarDoc/<int:id>/', deletarDoc, name='deletarDoc'),


    path('', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('', login, name='login'),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


