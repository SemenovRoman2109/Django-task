from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
class Comment(models.Model):
    author = models.CharField(max_length=255)
    content = models.CharField(max_length=255)