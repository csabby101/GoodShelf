from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    progress = models.CharField(max_length=20)
    notes = models.TextField(null=True, blank=True)
    CURRENT_STATUS = (
        ('C', 'Currently Reading'),
        ('R', 'Read'),
        ('T', 'To Be Read'),
    )
    status = models.CharField(max_length=1, choices=CURRENT_STATUS, default='T')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

