from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == "POST":
        user= auth.authenticate(username = request.POST['email'], password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            print("..........Wrong")
            return render(request,'login.html', {'error': 'Username or Password is not correct'})
        # print(request.POST['email'])
        # print(request.POST['password'])
        # return render(request, './login.html')
    else:
        return render(request, './login.html')