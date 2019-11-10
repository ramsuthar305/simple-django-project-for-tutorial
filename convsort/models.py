from django.db import models
import datetime


class REGISTRATIONS(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100,default="something")
    roll_no = models.CharField(max_length=100)
    cgpa= models.CharField(max_length=100)
    company_cgpa=models.CharField(max_length=100)
    user_type =models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    resume=models.CharField(max_length=100,default="NONE")


