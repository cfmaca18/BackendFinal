"""Banco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from proyectos.views.login import UserLoginAPIView
from proyectos.views.signup import UserSignUpAPIView
from proyectos.views.lista_proyecto import *
from proyectos.views.lista_entrega import *
from proyectos.views.lista_inscritos import *
from proyectos.views.lista_grupos import *
from proyectos.views.ficha_usuario import *
from proyectos.views.agregar_integrantes import *
from proyectos.views.integrantes import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('proyectos.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/login/', UserLoginAPIView.as_view(), name='login'),
    path('api/signup/', UserSignUpAPIView.as_view(), name='login'),
    path('api/proyectos/<int:user_id>/',ListaProyectosViewSet.as_view({'get':'get_usuario_proyectos'}), name='entregas_por_usuario_proyecto'),
    path('api/entregas/<int:id_proyecto>/', ListaEntregaViewSet.as_view({'get': 'get_entregas_por_proyecto'}), name='lista_entregas_por_proyecto'),
    path('api/inscritos/<int:id_user>/', ListaInscritosViewSet.as_view({'get': 'get_inscritos'}), name='lista_entregas_por_proyecto'),
    path('api/grupos/<int:id_user>/', ListaGruposViewSet.as_view({'get': 'get_mis_grupos'}), name='lista_entregas_por_proyecto'),
    path('api/agregar-integrantes/<int:id_user>/', AgregarIntegrantesViewSet.as_view({'get': 'get_inscritos'}), name='get_fichas_usuario'),
    path('api/integrantes/<int:grupo_id>/', IntegrantesViewSet.as_view({'get': 'get_integrantes'}), name='get_fichas_usuario'),

]

