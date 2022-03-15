from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import View, ListView
from django.shortcuts import get_object_or_404
from pages.models import Whisky, Rating, Distillery
import tkinter.messagebox
import time
from random import random
from tkinter import *

from django.contrib.auth import login, authenticate
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
        context = {}
        context['distilleries'] = Distillery.objects.all()

        return render(request, 'pages/index.html', context)


class ReviewView(View):
    def get(self, request, **kwargs):
        context = {}
        instance = get_object_or_404(Whisky, pk=kwargs.get('pk'))

        context['whisky'] = instance
        context['ratings'] = Rating.objects.filter(whisky_id=instance.pk)

        return render(request, 'pages/review.html', context)


class WhiskyList(ListView):
    template_name = 'templates/whisky_list.html'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        instance = get_object_or_404(Distillery, pk=self.kwargs.get('pk'))

        return Whisky.objects.filter(distillery=instance.pk)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = get_object_or_404(Distillery, pk=self.kwargs.get('pk'))

        context['distillery'] = instance

        return context


class ChoosingDistillery(View):
    def get(self, request, **kwargs):
        return render(request, 'pages/ChoosingDistillery.html')


def about(request):
    return render(request, 'pages/about.html')


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
            # password1 = make_password(password1)
            if not User.objects.filter(username=name).exists():
                User.objects.create_user(username=name, password=password1)
            new_user = models.User()
            new_user.nickname = name
            new_user.email = email
            new_user.password = password1
            new_user.save()
            return HttpResponseRedirect('/login/')


def change_password(request):
    if request.method == 'GET':
        return render(request, 'pages/changepassword.html')
    if request.method == 'POST':
        username = request.POST.get('user_name')
        old_password = request.POST.get('old_password')
        password1 = request.POST.get('new_password')
        password2 = request.POST.get('re_new_password')
        user = auth.authenticate(username=username, password=old_password)
        if user is not None and user.is_active:
            if password1 == password2:
                user.set_password(password1)
                user.save()
                return HttpResponseRedirect('/login/')
            else:
                tkinter.messagebox.showinfo('Hint', 'The two passwords are inconsistent!')
                return render(request, 'pages/changepassword.html')


def user_login(request):
    if request.method == 'GET':
        return render(request, 'pages/login.html')

    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     if models.User.objects.filter(nickname=username).exists():
    #         user = models.User.objects.get(nickname=username)
    #         if check_password(password, user.password):
    #             auth.login(request, user)
    #             return HttpResponseRedirect('/')
    #         else:
    #             tkinter.messagebox.showinfo('Hint', 'Incorrect password')
    #             return render(request, 'pages/login.html')
    #     else:
    #         tkinter.messagebox.showinfo('Hint', 'The email address does not exist')
    #         return render(request, 'pages/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            tkinter.messagebox.showinfo('Hint', 'Incorrect password')
            return render(request, 'pages/login.html')


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return HttpResponseRedirect('/login/')
