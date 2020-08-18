from django.db import models

# Create your models here.
class UserDetails(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    city=models.CharField(max_length=50,null=True)
    desc=models.TextField(blank=True,null=True)
    ref=models.CharField(max_length=200,null=True,blank=True)