from django.shortcuts import render
from django.http import HttpResponse
from .models import Course


class Course:
    def __init__(self, name, location, par, description):
        self.name = name
        self.location = location
        self.par = par
        self.description = description


courses = [
    Course('Admiral Baker', 'San Diego', 72, 'A navy golf course'),
    Course('Torrey Pines', 'San Diego', 72, 'Beautiful course on top of ocean cliff'),
    Course('Mission Bay', 'San Diego', 58, "Very short course with no par 5's"),
    Course('Mission Trails', 'San Diego', 72, 'Very Average'),
    Course('Balboa Golf Course', 'San Diego', 72, 'Greens are faster than the PGA greens')
]



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def course_index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})


