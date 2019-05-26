from django.urls import path

from . import views

urlpatterns = [

    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('student/<int:pk>/', views.studentprofile_detail, name='student-detail'),
    path('student/<int:pk>/update/', views.update_profile, name='update-profile'),
    path('student/<int:pk>/delete/', views.delete_profile, name='delete-profile'),
    path('student/', views.student_detail, name='student'),
    path('teacher/', views.teacher_detail, name='teacher'),
]