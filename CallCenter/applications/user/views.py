from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as dj_login

def principal(request):
    data = {}
    return render(request, 'user/principal.html', data)
