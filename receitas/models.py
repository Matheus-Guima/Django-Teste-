from pyexpat import model
from django.db import models
from datetime import datetime

# Create your models here.

class Receita(models.Model):
    nome_receitas = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_de_preparo = models.TextField()
    tempo_de_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_receita= models.DateTimeField(default=datetime.now, blank=True)
    