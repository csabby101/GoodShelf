from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    progress = models.CharField(max_length=20)
    notes = models.TextField(null=True, blank=True)
    read = models.BooleanField(default=False)
    to_be_read = models.BooleanField(default=False)
    currently_reading = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['read']
