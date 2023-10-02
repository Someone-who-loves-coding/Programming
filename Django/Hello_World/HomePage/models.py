from django.db import models
from datetime import datetime
class Contact(models.Model):
    name = models.CharField(max_length=122)
    Email= models.CharField(max_length=122)
    Comment=models.CharField(max_length=200)
    Date= models.DateField(default=datetime.now())