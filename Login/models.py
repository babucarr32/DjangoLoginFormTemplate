from django.db import models

class loginModel(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)