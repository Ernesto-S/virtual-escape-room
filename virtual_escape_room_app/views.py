from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
from django.db.models import Q
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

def results(request,id):
    # if 'usrname' not in request.session:
    #     return redirect('/')
    qryPlayer=Player.objects.get(id=id)
    qryThemes= Theme.objects.order_by('timer')
    qryPlayerUserName=qryPlayer.username
    print(qryPlayerUserName)
    if qryPlayer !='':
        qryAchievements=qryThemes.filter(Q(player__username__exact=qryPlayerUserName) & Q(status__exact='Success'))
        qryleader=qryThemes.filter(status__exact='Success')
        context={
            'queryachievements':qryAchievements,
            'queryleaderboard':qryleader
        }   
        print(qryAchievements)
        print(qryThemes)
        return render(request, "results.html",context)

