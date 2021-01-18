from django.db import models
from PIL import Image


class Hospital(models.Model):
    nome_hospital = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='img',null=True, blank=True)
    desc_hospital = models.TextField
    tipo_hospital = models.CharField(max_length=200)
    conceito_hospital = models.CharField(max_length=200)

def __str__(self):
    """Retorna uma representação de uma String do modelo."""
    return self.nome_hospital

