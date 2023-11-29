from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    device = models.CharField(max_length=255)

    def __str__(self):
        return f"Name: {self.name}, Entry device1: {self.device}"

