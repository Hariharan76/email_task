from django.db import models

class  mail(models.Model):
    first_name=models.CharField()
    last_name=models.CharField()
    email=models.EmailField( max_length=254)
    password=models.CharField()
    conform_password=models.CharField()
