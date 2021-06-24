from django.db import models

class ProductModel(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Car (models.Model):
    name = models.CharField(max_length=50)
    product = models.ForeignKey('ProductModel', on_delete=models.CASCADE)