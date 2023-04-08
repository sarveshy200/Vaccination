from django.db import models

# Create your models here.
class slotbooking(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField(max_length=60)
    date=models.CharField(max_length=60)
    time=models.CharField(max_length=60)
    strenght=models.IntegerField(max_length=60)
    class Meta:
        db_table="slotbooking"

class register(models.Model):
    email=models.EmailField(max_length=60)
    password=models.CharField(max_length=60)
    
    class Meta:
        db_table="register"

