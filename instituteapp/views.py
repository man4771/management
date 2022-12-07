from doctest import master
import email
from email.policy import default
from json import load
from tkinter.messagebox import showinfo, showwarning
from urllib import request
from urllib.robotparser import RequestRate
from django.shortcuts import render,redirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from random import randint

default_data = {
    'current_page' : None,
    'gender_choices' : [],
    'user_roles': UserRole.objects.all(),
    
}

def alert(type, text):
    default_data['alert'] = {
        'type': type,
        'text': text,
    }
    print('alert called.')

for gc in gender_choices:
    default_data['gender_choices'].append({'text_text' : gc[0] , 'text' : gc[1]})

print(default_data['gender_choices'])

# index
def index(request):
    default_data['current_page'] = 'index'
    return redirect(login_page)

# index page
def index_page(request):
    default_data['current_page'] = 'index_page'
    return render(request,'index_page.html',default_data)

# clubs page
def clubs_page(request):
    default_data['current_page'] = 'clubs_page'
    return render(request,'clubs_page.html',default_data)


# login page
def login_page(request):
    default_data['current_page'] = 'login_page'
    return render(request,'login_page.html',default_data)

# register page
def register_page(request):
    default_data['current_page'] = 'register_page'
    return render(request,'register_page.html',default_data)

# load profile data
def profile_data(request):
    master = Master.objects.get(Email = request.session['email'])
    student = Student.objects.get(Master = master)
    student_mat = Student_mat.objects.get()
    teacher_mat = Teacher_mat.objects.get()
    book = Book.objects.get()
    if master.Email:
        master.email
    default_data['profile_data'] = [student,student_mat,teacher_mat,book]



# profile page
def profile_page(request):
    if request.session['email']:
        default_data['current_page'] = 'profile_page'
        profile_data(request)
        return render(request,'profile_page.html',default_data)
    return redirect(login_page)

def profilee_page(request):
    if request.session['email']:
        default_data['current_page'] = 'profilee_page'
        dataaa(request)
        return render(request,'profilee_page.html',default_data)
    return redirect(login_page)

# teacher profile page load
def dataaa(request):
    master = Master.objects.get(Email = request.session['email'])
    teacher = Teacher.objects.get(Master = master)
    default_data['dataaa'] = teacher


# student page
def student_page(request):
        default_data['current_page'] = 'student_page'
        data(request)
        return render(request,'student_page.html',default_data)
    
# teacher page
def teacher_page(request):
        default_data['current_page'] = 'teacher_page'
        te_data(request)
        return render(request,'teacher_page.html',default_data)
    
# book page
def book_page(request):
        default_data['current_page'] = 'book_page'
        book(request)
        return render(request,'book_page.html',default_data)
    
    

def forgotpassword_page(request):
    default_data['current_page'] = 'forgotpassword_page'
    return render(request,'forgotpassword_page.html',default_data)

# change password
def change_password(request):
    master = Master.objects.get(Email = request.POST['email'])
    
    try:
        request.session['email'] = master.Email
        if master.Password == request.POST['current_password']:
            master.Password = request.POST['new_password']
            master.save()
        else:
            print("incorrect password")
        return redirect(profile_page)
    except:
        print('incorrect email id ')


    
# update student profile
def update_profile(request):
    master = Master.objects.get(Email = request.session['email'])
    student = Student.objects.get(Master = master)
    
    
    print('update data' , request.POST)

    student.Name = f"{request.POST['first_name']} {request.POST['last_name']}"
    student.Address = request.POST['address']
    student.Gender = request.POST['gender']
    student.Roll_number = request.POST['roll']

    
    
    student.save()
    
    return redirect(profile_page)

#  update teacher profile
def updatee_profile(request):
    master = Master.objects.get(Email = request.session['email'])
    teacherr = Teacherr.objects.get(Master = master)

    print('update data',request.POST)

    teacherr.Name = request.POST['name']
    
    
    teacherr.save()
    return redirect(profile_page)


# student login system
def login(request):
    master = Master.objects.get(Email = request.POST['email'])
    print(request.POST)
    try:
        request.session['email'] = master.Email
        if master.Isactive:
            if master.Password == request.POST['password']:
                return redirect(index_page)
            else:
                print("incorrect password")
                alert('warning','incorrect password')
        else:
            print("your account is inactive")
            
    except Master.DoesNotExist as err:
        alert('record not found')
    return redirect(login_page)

# student register system
def register(request):
    print(request.POST)
    userrole = UserRole.objects.get(id=int(request.POST['userrole']))
    master = Master.objects.create(
                UserRole = userrole,
                Email = request.POST['email'],
                Password = request.POST['password'],
                Isactive = True,
            )
        
    

    
    master.save()
    request.session['email'] = request.POST['email']
    
    print(request, 'register')
   
    # verify_otp(request)

    
    
    return redirect(login_page)

def otp_page(request):
    default_data['current_page'] = 'otp_page'
    return render(request, 'otp_page.html', default_data)

# OTP Creation
def otp(request):
    otp_number = randint(1000, 9999)
    print("OTP is: ", otp_number)
    request.session['otp'] = otp_number

# send_otp
def send_otp(request, otp_for="register"):
    print(otp_for)
    otp(request)

    email_to_list = [request.session['email'],]

    if otp_for == 'activate':
        request.session['otp_for'] = 'activate'
        subject = f'OTP for  Account Activation'
    elif otp_for == 'recover_pwd':
        request.session['otp_for'] = 'recover_pwd'
        subject = f'OTP for  Password Recovery'
    else:
        request.session['otp_for'] = 'register'
        subject = f'OTP for  Registration'

    email_from = settings.EMAIL_HOST_USER

    message = f"Your One Time Password for verification is: {request.session['otp']}."

    send_mail(subject, message, email_from, email_to_list)

    alert('success', 'An OTP has sent to your email.')

    
    # default_data.update({'next_step': 'otp'})
    
    # return JsonResponse(data)
    # return redirect(otp_page)

# verify otp
def verify_otp(request, verify_for="register"):

    if request.session['otp'] == int(request.POST['otp']):

        if verify_for == 'activate':
            master = Master.objects.get(Email=request.session['email'])
            master.IsActive = True
            master.save()


            return redirect(profile_page)
        elif verify_for == 'recover_pwd':
            master = Master.objects.get(Email=request.session['email'])
            master.Password = request.session['password']
            master.save()
        else:
            user_role = UserRole.objects.get(id=int(request.session['reg_data']['userrole']))
            master = Master.objects.create(
                UserRole = user_role,
                Email = request.session['reg_data']['email'],
                Password = request.session['reg_data']['password'],
                IsActive = True,
            )

            Student.objects.create(
                Master = master,
            )

        print("verified.")
        alert('success', 'An OTP verified.')

    else:
        print("Invalid OTP")
        
        alert('danger', 'Invalid OTP')

        return redirect(otp_page)
    
    return redirect(login_page)




# profile data
def profile_data(request):
    master = Master.objects.get(Email = request.session['email'])
    student = Student.objects.get(Master = master)
    
    if student.Name: 
        splitted_names = student.Name.split()
        student.FirstName = splitted_names[0]
        
        if len(splitted_names) > 1:
            student.LastName = splitted_names[1]

    default_data['profile_data'] = student

# student page
def data(request):
    student_mat = Student_mat.objects.get()
    default_data['data'] = student_mat

# teacher page
def te_data(request):
    teacher_mat = Teacher_mat.objects.get()
    default_data['te_data'] = teacher_mat

# book page
def book(request):
    book_mat = Book.objects.get()
    default_data['book'] = book_mat

# logout
def logout(request):
    if 'email' in request.session:
        del request.session['email']
    return redirect(login_page)

# teacher login system
def loginn(request):
    viewer = Viewer.objects.get(Email = request.POST['email'])
    print(request.POST)
    
    try:
        request.session['email'] = viewer.Email
        if viewer.Isactive:
            if viewer.Password == request.POST['password']:
                return redirect(index_pagee)
            else:
                print('incorrect password')
        else:
            print('your account is not active')
    except Viewer.DoesNotExist as err:
        print('incorrect email')
        return redirect(login_pagee)

# teacher login page
def login_pagee(request):
    default_data['current_page'] = 'login_pagee'
    return render(request,'login_pagee.html',default_data)

# teacher index page
def index_pagee(request):
        default_data['current_page'] = 'index_pagee'
        return render(request,'index_pagee.html',default_data)

# teacher register page
def registerr(request):
    print(request.POST)
    userrole = UserRole.objects.get(id=int(request.POST['userrole']))
    viewer = Viewer.objects.create(
                UserRole = userrole,
                Email = request.POST['email'],
                Password = request.POST['password'],
                Isactive = True,
            )
        
    

    
    viewer.save()
    request.session['email'] = request.POST['email']
    
    print(request, 'registerr')
    return redirect(login_pagee)

# teacher register page
def registerr_page(request):
    default_data['current_page'] = 'registerr_page'
    return render(request,'registerr_page.html',default_data)

def log_out(request):
    viewer = Viewer.objects.get(Email = request.session['email'])

    if request.session['email'] == viewer.Email:
        del request.session['email']
    return redirect(login_pagee)

def change_p_page(request):
    default_data['current_page'] = 'change_p_page'
    return render(request,'change_p_page.html',default_data)

def change_passwordd(request):
    viewer = Viewer.objects.get(Email = request.POST['email'])
    print(request.POST)
    try:
        request.session['email'] = viewer.Email
        if viewer.Password == request.POST['current_password']:
            viewer.Password = request.POST['new_password']
            viewer.save()
            return redirect(index_pagee)
        else:
            print('incorrect password')
            return redirect(login_pagee)
    except Viewer.DoesNotExist as err:
        return redirect(login_pagee)



        
    





    




    



