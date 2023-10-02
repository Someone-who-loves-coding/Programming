from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=122)
    Email= models.CharField(max_length=122)
    Phone= models.IntegerField()
    Subject=models.CharField(max_length=200)
