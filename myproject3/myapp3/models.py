from django.db import models

# Create your models here.
class Mymodel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name
    
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    password = models.CharField(max_length=100)
   

    def __str__(self):
        return self.username