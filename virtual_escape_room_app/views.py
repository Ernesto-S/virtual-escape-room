from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.
def redirect_to_virtual_escape_room(request): # url ''
    #return HttpResponse("Redirect to landing page")
    return render(request,"landing.html")


def show_landing_page(request): # url 'virtual_escape_room'
    return HttpResponse("Show landing page")

def login(request): # url 'virtual_escape_room/login'
    return HttpResponse("Log me in")

def register(request): # url 'virtual_escape_room/register'
    return HttpResponse("Register me")

def logout(request): # url 'virtual_escape_room/logout'
    return HttpResponse("Log me out")

def get_data(request):
    qry_players= Player.objects.all()
    qry_themes=Theme.objects.all()
    qry_puzzles=Puzzles.objects.all()
    context={
            'queryplayers':qry_players,
            'querythemes':qry_themes,
            'querypuzzles':qry_puzzles
        }   
    return render(request, "get_data.html", context)
