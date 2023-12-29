from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=60, blank=True , null=True)
    standard = models.CharField(max_length=60,blank=True, null=True)
    blood_Group = models.CharField(max_length=60,blank=True, null=True)
    address = models.CharField(max_length=100,blank=True,null=True)

    def __str__ (self):
        return self.name