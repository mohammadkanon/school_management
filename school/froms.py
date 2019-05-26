from django import forms
from .models import TeacherProfile, StudentProfile

class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['first_name', 'last_name', 'gender', 'department']



class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth']

