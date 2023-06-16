from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.lista_entregas import *

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

class ListaEntregaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Entrega.objects.all()
    serializer_class = ListaEntregaSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_entregas_por_proyecto(self, request, *args, **kwargs):
        id_proyecto = kwargs['id_proyecto']
        entregas = Entrega.objects.filter(proyecto=id_proyecto)
        serializer = ListaEntregaSerializer(entregas, many=True)
        return Response(serializer.data)
