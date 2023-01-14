from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def login(request):
    return render(request, 'login.html')