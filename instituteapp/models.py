from email.policy import default
from random import choices
from secrets import choice
from tkinter import CASCADE
from xmlrpc.client import MultiCallIterator
from django.db import models

class UserRole(models.Model):
    Role = models.CharField(max_length=10)

    class Meta:
        db_table = 'userrole'

    def __str__(self) -> str:
        return self.Role

class Master(models.Model):
    UserRole = models.ForeignKey(UserRole , on_delete=models.CASCADE)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=12)
    Isactive = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'master'

    def __str__(self) -> str:
        return self.Email

class Viewer(models.Model):
    UserRole = models.ForeignKey(UserRole , on_delete=models.CASCADE)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=12)
    Isactive = models.BooleanField(default=False)

    class Meta:
        db_table = 'viewer'

    def __str__(self) -> str:
        return self.Email

gender_choices = (
    ('m' , 'male'),
    ('f' , 'female'),
)


class Student(models.Model):
    Master = models.ForeignKey(Master , on_delete=models.CASCADE)
    Name = models.CharField(default='',max_length=255,blank=True)
    Date_of_birth = models.DateField()
    Date_of_joining = models.DateField()
    Address = models.TextField()
    Gender = models.CharField(max_length=5,choices=gender_choices)
    Roll_number = models.IntegerField()


    class Meta:
        db_table = 'student'

class Teacher(models.Model):
    Master = models.ForeignKey(Master , on_delete=models.CASCADE)
    Name = models.CharField(default='',max_length=255,blank=True)
    Date_of_birth = models.DateField()
    Date_of_joining = models.DateField()
    Address = models.TextField()

    class Meta:
        db_table = 'teacher'

# Create your models here.

class Student_mat(models.Model):
    Subject = models.CharField(max_length=120)
    Attendens = models.CharField(max_length=120)
    Assignment = models.CharField(max_length=120)
    Marks = models.IntegerField(max_length=120)

    class Meta:
        db_table = 'student_mat'

class Teacher_mat(models.Model):
    Subject = models.CharField(max_length=120)
    Complate_assignment = models.CharField(max_length=120)
    Pendding_assigment = models.CharField(max_length=120)
    Exam = models.IntegerField(max_length=120)

    class Meta:
        db_table = 'teacher_mat'

class Book(models.Model):
    Subject = models.CharField(max_length=120)

    class Meta:
        db_table = 'book'

class Teacherr(models.Model):
    Master = models.ForeignKey(Master , on_delete=models.CASCADE)
    Name = models.CharField(default='',max_length=255,blank=True)


    class Meta:
        db_table = 'teacherr'