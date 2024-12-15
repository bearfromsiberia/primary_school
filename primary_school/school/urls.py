from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    path('', views.index, name='index'),
    path('classes/', views.class_list, name='class_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teacher/<int:teacher_id>/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student/<int:student_id>/', views.student_dashboard, name='student_dashboard'),
    path('parent/<int:parent_id>/', views.parent_dashboard, name='parent_dashboard'),
]