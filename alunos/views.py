from alunos.models import Alunos
from alunos.serializers import AlunosSerializer

from rest_framework import viewsets

class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer
                    