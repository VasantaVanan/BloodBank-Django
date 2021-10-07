from django.db import models

# Create your models here.
class Doner(models.Model):
    name = models.CharField(max_length=30)
    blood_group = models.CharField(max_length=15)
    age = models.IntegerField(default=18)
    address = models.TextField()
    contact_no = models.IntegerField()
