from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todolist', null=True)
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('todolist-details', args=[self.pk])


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
