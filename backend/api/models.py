from django.db import models

# Create your models here.

class File(models.Model):
    Filename=(models.CharField(max_length=100, blank=True, null=True))
    