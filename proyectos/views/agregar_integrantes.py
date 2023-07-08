from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from proyectos.serializers.lista_inscritos import ListaInscritoSerializer
from proyectos.models import Inscrito
from proyectos.views.funciones import perfil_conectado

class AgregarIntegrantesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Inscrito.objects.all()
    serializer_class = ListaInscritoSerializer

    @action(detail=False, methods=['get'], url_path='inscritos/(?P<id_user>\d+)')
    def get_inscritos(self, request, id_user=None):
        # Obtener el perfil_id del usuario logueado
        perfil_id = perfil_conectado(id_user)

        inscrito = Inscrito.objects.get(perfil = perfil_id)
        print ("xxxxxxxxx")
        cod_ficha = inscrito.ficha.codigo
        print (cod_ficha)
        print ("xxxxxxxxx")
        # Obtener los inscritos que no son el usuario logueado y cumplen las condiciones
        inscritos = Inscrito.objects.exclude(perfil_id=perfil_id).filter(estado='activo', nombre_grupo__isnull=True, ficha__codigo = cod_ficha )

        # Serializar los datos de los inscritos
        serializer = self.get_serializer(inscritos, many=True)

        # Devolver la respuesta con los datos serializados
        return Response(serializer.data)