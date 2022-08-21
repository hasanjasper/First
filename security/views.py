from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.paginator import Paginator
from django.core.mail import send_mail,EmailMessage
from .forms import *
from .models import *
from django.utils.decorators import method_decorator
from django.http import *
from django.template.loader import render_to_string
from django.db.models import Q


def register(request):
    if request.method == 'POST':
        form = register_users(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(username=data['name'],email=data['email'],password=data['password_2'])
            return redirect('security:join')
    else:
        form = register_users()
    return render(request,'security/register.html',{'form':form})



def join(request):
    user = request.user
    if request.method == 'POST':
        form = join_users(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data['user_name'],password=data['user_password'])
            if user is not  None:
                login(request,user)
                return redirect('website:home')

    else:
        form = join_users
    return render(request,'security/join.html',{'form':form})



