from alunos.models import Alunos
from rest_framework import serializers

class AlunosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alunos
        fields = '__all__'