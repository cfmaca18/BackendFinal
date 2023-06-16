from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.grupo import *

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

class ListaGruposViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_mis_grupos(self, request, *args, **kwargs):
        perfil_id =  kwargs['id_user']
        grupos = Grupo.objects.filter(integrantes__perfil_id=perfil_id)
        serializer = GrupoSerializer(grupos, many=True)
        return Response(serializer.data)
