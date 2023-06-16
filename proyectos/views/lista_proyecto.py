from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.proyecto import *

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

class ListaProyectosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_usuario_proyectos(self, request, *args, **kwargs):
        perfil_id =  kwargs['id_user']
         


