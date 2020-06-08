from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Offer(models.Model):
    codename = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
