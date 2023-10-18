from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    parent = models.ForeignKey('Task', null=True, on_delete=models.CASCADE,
                               related_name='children') # jeśli parent == None to ten task jest traktowany jak projekt
    done = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class TimeSpent(models.Model):
    amount = models.IntegerField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=512)

class Cost(models.Model):
    description = models.TextField()
    amount = models.FloatField()
    task = models.ForeignKey(Task,on_delete=models.CASCADE)


def check_length_of_str(value):
    if len(value) < 4:
        raise ValidationError('za krótki')

class Resource(models.Model):
    name = models.CharField(max_length=128, validators=[check_length_of_str])
    description = models.TextField()
    price = models.FloatField()



