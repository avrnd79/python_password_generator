from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    thepassword = ''
    lenght = int(request.GET.get('lenght'), 10)
    chars = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        chars.extend(list('!@#$%^&*()_+=-{}[]<>?'))

    if request.GET.get('numbers'):
        chars.extend(list('0123456789'))

    for _ in range(lenght):
        thepassword += random.choice(chars)
    return render(request, 'generator/password.html', {'password': thepassword})
