from django.contrib import admin
from .models import *

admin.site.site_title = 'Management_Institute'
admin.site.site_header = 'Management_Institute'

mymoodels = [UserRole,Master,Viewer,Student,Teacher,Student_mat,Teacher_mat,Book,Teacherr]

for model in mymoodels:
    admin.site.register(model)
# Register your models here.
