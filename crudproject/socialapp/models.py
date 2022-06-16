from django.db import models

class Signup(models.Model):
    name=models.TextField(max_length=10)
    username=models.TextField(max_length=10)
    password=models.TextField(max_length=8)
    confirmpassword=models.TextField(max_length=8)
   
   
    class Meta:
        db_table='signup'
