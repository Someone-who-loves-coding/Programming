from django.db import models

class Form(models.model):
    name = models.CharField(max_length=122)
    Email= models.CharField(max_length=122)
    Phone= models.IntegerField(max_length=10)
    Subject=models.CharField()
