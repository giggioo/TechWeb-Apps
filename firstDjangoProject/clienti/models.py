from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)
    