# reviews/models.py
from django.db import models
from products.models import Product

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
