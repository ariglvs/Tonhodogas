from django.db import models

class Teste(models.Model):
    teste2 = models.CharField('teste2', max_length=100)
    teste3 = models.IntegerField('teste3')