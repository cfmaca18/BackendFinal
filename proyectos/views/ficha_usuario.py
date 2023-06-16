from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.lista_inscritos import *

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response


from django.shortcuts import get_object_or_404

from proyectos.views.funciones import *

class FichasUsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Inscrito.objects.all()
    serializer_class = ListaInscritoSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_fichas_usuario(self, request, *args, **kwargs):
        perfil_id =  kwargs['id_user']
        inscritos = Inscrito.objects.filter(perfil_id=perfil_id)
 
        # Serializar los datos de los inscritos
        serializer = self.get_serializer(inscritos, many=True)
        return Response(serializer.data)
