from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Course
from .forms import CourseForm


# class Course:
#     def __init__(self, name, location, par, description):
#         self.name = name
#         self.location = location
#         self.par = par
#         self.description = description


# courses = [
#     Course('Admiral Baker', 'San Diego', 72, 'A navy golf course'),
#     Course('Torrey Pines', 'San Diego', 72, 'Beautiful course on top of ocean cliff'),
#     Course('Mission Bay', 'San Diego', 58, "Very short course with no par 5's"),
#     Course('Mission Trails', 'San Diego', 72, 'Very Average'),
#     Course('Balboa Golf Course', 'San Diego', 72, 'Greens are faster than the PGA greens')
# ]



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def course_index(request):
    courses = Course.objects.all()  # Get all courses
    return render(request, 'courses/index.html', {'courses': courses})

def course_detail(request, course_id):
    # course = Course.objects.get(id=course_id)
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/detail.html', {'course': course} )

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course-index')  # Redirect to courses page after saving
    else:
        form = CourseForm()

    return render(request, 'courses/course_form.html', {'form': form})


