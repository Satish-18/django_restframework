from pyexpat import model
from tkinter.tix import Tree
from django.db import models

# Create your models here.

class Details(models.Model):
    task = models.CharField(max_length=100,blank=True)
    attandence = models.CharField(max_length=100,blank=True)
    task_completed = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.task


class UserProfile(models.Model):
   
    intern = models.CharField(max_length=100)

    def __str__(self):
        return self.intern
