from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

class Product(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    image_url = models.CharField(max_length=500, blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='products')
