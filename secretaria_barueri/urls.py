from django.contrib import admin
from django.urls import path
from usuarios.views import *
from vaga.views import *

urlpatterns = [
    path('cadastro/pf',cadastrar_pessoa_fisica),
    path('cadastro/pf/acessibilidade', acessibilidade_cadastro),
    path('cadastro/pj', cadastrar_empresa),
    path('cadastro/vaga', cadastro_vaga),
    path('admin/', admin.site.urls),
]
