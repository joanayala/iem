from django.db import models

class people(models.Model) :
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    id_type = models.IntegerField()
    number_id = models.CharField(max_length=100)
    address = models.CharField(max_length=100, default = "")
    email = models.CharField(max_length=100, default="")