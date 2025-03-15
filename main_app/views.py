from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Course
from .forms import CourseForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy


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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to user's courses after signup
    else:
        form = UserCreationForm()
    
    return render(request, 'users/signup.html', {'form': form})


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def course_index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})

@login_required
def user_courses(request):
    courses = Course.objects.filter(user=request.user) 
    return render(request, 'courses/user_courses.html', {'courses': courses})

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'courses/detail.html', {'course': course} )

class CourseCreate(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign logged-in user as course creator
        return super().form_valid(form)


class CourseUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    form_class = CourseForm

    def test_func(self):
        course = self.get_object()
        return self.request.user == course.user  # Only allow owner to edit

class CourseDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('user-courses')  
    template_name = 'courses/course_confirm_delete.html'

    def test_func(self):
        course = self.get_object()
        return self.request.user == course.user  # Only allow owner to delete
    

