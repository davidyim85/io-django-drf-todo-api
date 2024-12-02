from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    subject=models.CharField(max_length=200)
    details=models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="todos")