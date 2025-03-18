from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('top-courses/', views.course_index, name='course-index'), 
    path('user-courses/', views.user_courses, name='user-courses'), 
    path('courses/<int:course_id>/', views.course_detail, name='course-detail'),
    path('courses/create/', views.CourseCreate.as_view(), name='course-create'),
    path('courses/<int:pk>/update/', views.CourseUpdate.as_view(), name='course-update'),
    path('courses/<int:pk>/delete/', views.CourseDelete.as_view(), name='course-delete'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': 'home'}, name='logout'),
    path('signup/', views.signup, name='signup'),
]
