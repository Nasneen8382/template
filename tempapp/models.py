from django.db import models

# Create your models here.
class Theme(models.Model):
    name=models.CharField(max_length=400)
    status=models.CharField(max_length=200,default='inactive..')