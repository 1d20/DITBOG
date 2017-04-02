from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.core.urlresolvers import reverse


def home(request):
    return render(request, 'core/home.html', {})


def login(request):
    return render(request, 'core/login.html', c)


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('themes'))
    return HttpResponseRedirect(reverse('login'))


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))