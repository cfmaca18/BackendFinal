
from rest_framework import viewsets
from proyectos.models import Inscrito
from proyectos.serializers.inscritos import InscritoSerializer

class InscritoViewSet(viewsets.ModelViewSet):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer