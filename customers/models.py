# customers/models.py
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)
    loyalty_points = models.PositiveIntegerField(default=0) 

    def __str__(self):
        return f"{self.name} ({self.phone})"
