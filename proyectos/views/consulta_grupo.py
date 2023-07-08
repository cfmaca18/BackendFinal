from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from proyectos.models import Grupo

class CrearGrupoConsultaView(APIView):
    def post(self, request):
        usuario = request.user

        # Verificar si el usuario ya tiene un grupo asociado
        if Grupo.objects.filter(creador=usuario).exists() or Grupo.objects.filter(miembros=usuario).exists():
            return Response("El usuario ya tiene un grupo asociado", status=status.HTTP_400_BAD_REQUEST)
        
        # Lógica adicional para crear el grupo y agregar al usuario
        
        return Response("Grupo creado exitosamente", status=status.HTTP_201_CREATED)
