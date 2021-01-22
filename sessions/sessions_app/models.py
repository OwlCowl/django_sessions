from django.db import models

# Create your models here.

class SessionTbl(models.Model):
    key = models.CharField(max_length=45)
    value = models.IntegerField()

