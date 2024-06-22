from django.db import models


class Signup(models.Model):
  firstname = models.CharField(max_length=10)
  lastname = models.CharField(max_length=10)
  email =models.EmailField()
  phone_number = models.CharField(max_length=10) 
  password = models.CharField(max_length=6)
  confirm_password=models.CharField(max_length=6)