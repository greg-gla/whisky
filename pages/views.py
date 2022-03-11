import tkinter.messagebox
import time
from random import random
from tkinter import *

from django.contrib.auth import login
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.

from pages import models
from pages.forms import RegisterForm


class IndexView(View):
	def get(self, request, **kwargs):
		return render(request, 'pages/index.html')


def about(request):
	return render(request, 'pages/about.html')
    def get(self, request, **kwargs):
        return render(request, 'pages/index.html')


def regist(request):
    if request.method == 'GET':
        return render(request, 'pages/registration.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('re_password')
        if password1 != password2:
            tkinter.messagebox.showinfo('Hint', 'The two passwords are inconsistent!')
            return render(request, 'pages/registration.html')
        else:
            same_name_user = models.User.objects.filter(nickname=name)
            if same_name_user:
                tkinter.messagebox.showinfo('Hint', 'The user name is occupied!')
                return render(request, 'pages/registration.html')
            same_email_user = models.User.objects.filter(email=email)
            if same_email_user:
                tkinter.messagebox.showinfo('Hint', 'The email address has been registered!')
                return render(request, 'pages/registration.html')
            password1 = make_password(password1)
            new_user = models.User()
            new_user.nickname = name
            new_user.email = email
            new_user.password = password1
            new_user.save()
            return HttpResponseRedirect('/whisky/login/')


def user_login(request):
    if request.method == 'GET':
        return render(request, 'pages/login.html')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if models.User.objects.filter(email=email).exists():
            user = models.User.objects.get(email=email)
            if check_password(password, user.password):
                return render(request, 'pages/index.html')
            else:
                tkinter.messagebox.showinfo('Hint', 'Incorrect password')
                return render(request, 'pages/login.html')
        else:
            tkinter.messagebox.showinfo('Hint', 'The email address does not exist')
            return render(request, 'pages/login.html')