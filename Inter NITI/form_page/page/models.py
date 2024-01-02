from django.db import models

# Create your models here.


class info(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    lname=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name