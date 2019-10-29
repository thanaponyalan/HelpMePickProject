from django.db import models

from django_random_queryset import RandomManager

# Create your models here.
import os

def get_image_path(instance, filename):
    return os.path.join('static/activities', str(instance.id), filename)

class Activity(models.Model):
    objects=RandomManager()
    name=models.CharField(max_length=300)
    pict=models.ImageField(upload_to=get_image_path, blank=True,null=True)
    desc=models.CharField(max_length=300)
    ageRange=models.IntegerField()
    actType=models.IntegerField()

    def __str__(self):
        return self.name


class Food(models.Model):
    name=models.CharField(max_length=300)

    def __str__(self):
        return self.name