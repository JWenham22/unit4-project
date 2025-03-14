from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    par = models.IntegerField()
    description = models.TextField(max_length=250)
    image_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name
