from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.
def redirect_to_virtual_escape_room(request): # url ''
    return redirect('/virtual_escape_room')

def show_landing_page(request): # url 'virtual_escape_room'
    return render(request, 'landing.html')

def login(request): # url 'virtual_escape_room/login'
    return HttpResponse("Log me in")

def register(request): # url 'virtual_escape_room/register'
    return HttpResponse("Register me")

def logout(request): # url 'virtual_escape_room/logout'
    return HttpResponse("Log me out")