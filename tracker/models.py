from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    parent = models.ForeignKey('Task', null=True, on_delete=models.CASCADE,
                               related_name='children') # jeśli parent == None to ten task jest traktowany jak projekt

    def __str__(self):
        return self.name

class TimeSpent(models.Model):
    amount = models.IntegerField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=512)



