from django.db import models

# Create your models here.
class TeacherProfile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Gender_Choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    gender = models.CharField(max_length=6, choices=Gender_Choices, default=None)
    Department_Choices = [
        ('English', 'English'),
        ('Biology', 'Biology'),
        ('Philosophy', 'Philosophy'),
        ('Economy', 'Economy'),
        ('Bangla', 'Bangla'),
        ('Physics', 'Physics'),
    ]
    department = models.CharField(max_length=10, choices=Department_Choices, default=None)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class StudentProfile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Gender_Choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    gender = models.CharField(max_length=6, choices=Gender_Choices, default=None)
    date_of_birth = models.DateTimeField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)