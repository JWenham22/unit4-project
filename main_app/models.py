from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    par = models.IntegerField()
    description = models.TextField(max_length=250)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_top_course = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'course_id': self.id})
