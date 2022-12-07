from django.urls import path
from .views import *

urlpatterns = [
    
    path('',index,name=''),
    path('index_page/',index_page,name='index_page'),
    path('login_page/',login_page,name='login_page'),
    path('login_pagee/',login_pagee,name='login_pagee'),
    path('register_page/',register_page,name='register_page'),
    path('registerr_page/',registerr_page,name='registerr_page'),
    path('forgotpassword_page/', forgotpassword_page,name='forgotpassword_page'),
    path('change_p_page/', change_p_page,name='change_p_page'),
    path('profile_page/',profile_page,name='profile_page'),
    path('profilee_page/',profilee_page,name='profilee_page'),
    path('update_profile/',update_profile,name='update_profile'),
    path('updatee_profile/',updatee_profile,name='updatee_profile'),
    path('login/',login,name='login'),
    path('loginn/',loginn,name='loginn'),
    path('register/',register,name='register'),
    path('registerr/',registerr,name='registerr'),
    path('otp_page/', otp_page, name="otp_page"),
    path('student_page/',student_page,name='student_page'),
    path('teacher_page/',teacher_page,name='teacher_page'),
    path('clubs_page/',clubs_page,name='clubs_page'),
    path('book_page/',book_page,name='book_page'),
    path('verify_otp/<str:verify_for>/', verify_otp, name="verify_otp"),
    path('change_password/',change_password,name='change_password'),
    path('change_passwordd/',change_passwordd,name='change_passwordd'),
    path('logout/',logout,name='logout'),
    path('index_pagee/',index_pagee,name='index_pagee'),
    
]
