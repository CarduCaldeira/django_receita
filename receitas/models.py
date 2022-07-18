from django.db import models

# Create your models here.
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Receita(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_receita  = models.CharField(max_length = 200)
    ingredientes  = models.TextField()
    tempo_preparo = models.IntegerField()
    modo_preparo = models.TextField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_receita = models.DateTimeField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)
    foto_receita = models.ImageField(upload_to = 'fotos/%Y/%m/%d', blank = True)

    def __str__(self):
        return self.nome_receita
