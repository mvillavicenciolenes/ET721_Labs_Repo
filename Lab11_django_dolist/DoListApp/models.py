# DoListApp/models.py
from django.db import models

class ToDolist(models.Model):
    text = models.CharField(max_length=45)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text