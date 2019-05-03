from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=35)
    clas=models.CharField(max_length=35)
    age=models.IntegerField()
    place=models.CharField(max_length=35)
    mobile=models.BigIntegerField(max_length=100)
    # mobile = models.IntegerField()
    def __str__(self):
        return self.name

class teachers(models.Model):
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    age=models.IntegerField()
    place=models.CharField(max_length=35)
    mobile=models.BigIntegerField(max_length=100)
    # mobile = models.IntegerField()
    def __str__(self):
        return self.name




