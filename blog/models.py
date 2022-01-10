from django.db import models
from django.utils import timezone
# Create your models here.
class BlogProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

