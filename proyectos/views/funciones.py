# def usuario_inscrito_conectado(funcion):
#     def nueva_funcion(a, b):
#         print("Se va a llamar")
#         c = funcion(a, b)
#         print("Se ha llamado")
#         return c
#     return nueva_funcion

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User 
from proyectos.models import Entrega, Proyecto, Inscrito, Perfil


def perfil_conectado(user_id):
    user = get_object_or_404(User, id=user_id)
    perfil = get_object_or_404(Perfil, usuario=user)
    # inscrito = Inscrito.objects.filter(perfil = per)
    # inscrito = Inscrito.objects.filter(perfil__usuario__id = user_id)
    return perfil
    

