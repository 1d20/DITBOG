from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.core.context_processors import csrf


def index(request):
    if request.user is not None:
        if request.user.is_active:
            return HttpResponseRedirect('/theme/themes/')
    return HttpResponseRedirect('/login/')


def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'guest/login.html', c)


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return HttpResponseRedirect('/theme/themes/')
    return HttpResponseRedirect('/login/')


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login/')