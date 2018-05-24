from django.db import models


class User_info(models.Model):
    email = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    name = models.CharField(max_length=20,default='')


