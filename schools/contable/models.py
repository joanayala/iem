from django.db import models

# Create your models here.
class Cuentas(models.Model):
    tipo_cuenta = models.IntegerField()