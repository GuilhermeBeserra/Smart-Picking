from django.db import models

class usuarios(models.Model):
    nome= models.CharField(max_length=255)
    matricula= models.PositiveIntegerField(max_length=10)
    senha= models.CharField(max_length=15)
    email= models.EmailField()