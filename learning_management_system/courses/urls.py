from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_courses, name='courses'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('enroll/<int:course_id>/', views.enroll_to_course,
         name='enroll_to_course'),
    path('add/', views.add_course, name='add_course'),
    path('edit/<int:course_id>/', views.edit_course,
         name='edit_course'),
]
