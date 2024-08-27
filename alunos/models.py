from django.db import models

class Alunos(models.Model):
    nome = models.CharField(max_length=255)
    status = models.CharField(max_length=1)
    data = models.DateTimeField(auto_now_add=True)
