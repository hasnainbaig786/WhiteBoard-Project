from django.db import models

# Create your models here.
class Name(models.Model):    
    name = models.CharField(max_length=125,null=True,blank=True)
    email = models.EmailField(max_length=254,null=True,blank=True)
    password = models.BooleanField
    def __str__(self):
        return self.name
