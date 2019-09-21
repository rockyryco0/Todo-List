from django.db import models


# Create your models here.

class ToDo(models.Model):
    id_todo = models.AutoField(max_length=10, primary_key=True, null=False)
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)
