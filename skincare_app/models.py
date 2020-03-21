from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=2)
