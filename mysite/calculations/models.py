from django.db import models


class Prices20(models.Model):
    mark = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    profile = models.CharField(max_length=10)
    price = models.CharField(max_length=10)


class Prices30(models.Model):
    mark = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    profile = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
