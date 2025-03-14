from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.course_index, name='course-index'),
    path('courses/<int:course_id>/', views.course_detail, name='course-detail'),
    path('courses/add/', views.course_create, name='course-create'),
]