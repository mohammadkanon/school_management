from django.contrib import auth
from django.http import Http404
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .froms import TeacherForm, StudentForm
from .models import StudentProfile

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        this_user = auth.authenticate(username=username, password=password)

        if this_user is not None:
            auth.login(request, this_user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, 'school/login.html')

def home(request):
    context = {
        'students': StudentProfile.objects.all()
    }
    return render(request, 'school/home.html', context)

def studentprofile_detail(request, pk):
    this_student = get_object_or_404(StudentProfile, pk=pk)

    context = {
        'this_student': this_student
    }
    return render(request, 'school/studentprofile_detail.html', context)

def update_profile(request, pk):
    profile = get_object_or_404(StudentProfile, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=profile)
        if form.is_valid():
            profile.save()
            return redirect('student-detail', pk=pk)
    else:
        form = StudentForm(instance=profile)
    return render(request, 'school/student.html', {'form': form})

def delete_profile(request, pk):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    profile = get_object_or_404(StudentProfile, pk=pk)
    context = {
        'profile': profile
    }

    if request.method == 'POST':
        profile.delete()
        return redirect('home')

    return render(request, 'school/student_delete.html', context)

def student_detail(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()

    return render(request, 'school/student.html', {'form': form})

def teacher_detail(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TeacherForm()
    return render(request, 'school/teacher.html', {'form': form})