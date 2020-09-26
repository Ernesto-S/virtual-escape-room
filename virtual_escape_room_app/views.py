from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.
def redirect_to_virtual_escape_room(request): # url ''
    return redirect('/virtual_escape_room')

def show_landing_page(request): # url 'virtual_escape_room'
    try:
        if request.session['player_id'] > 0: 
            context = {
                'player': Player.objects.get(id=request.session['player_id']),
            }
            return render(request, 'landing.html', context)
    except:
        return render(request, 'landing.html')
    

def login(request): # url 'virtual_escape_room/login'
    if request.method == 'POST':
        logged_player = Player.objects.filter(email=request.POST['email'])
        if len(logged_player) > 0:
            logged_player = logged_player[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_player.password.encode()):
                request.session['player_id'] = logged_player.id
                return redirect('/virtual_escape_room')
            else:
                messages.error(request, 'Invalid Password')
                return redirect('/virtual_escape_room')
        else:
            messages.error(request, 'Invalid Email')
            return redirect('/virtual_escape_room')
    return redirect('/virtual_escape_room')

def register(request): # url 'virtual_escape_room/register'
    if request.method == 'POST':
        errors = Player.objects.player_validator(request.POST)
        if len(errors) > 0:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/virtual_escape_room')
        else:
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            new_player = Player.objects.create(
                username=request.POST['username'],
                email=request.POST['email'],
                password=hashed_pw
            )
            request.session['player_id'] = new_player.id
            
            return redirect('/virtual_escape_room')
    return redirect('/virtual_escape_room')

def logout(request): # url 'virtual_escape_room/logout'
    request.session.flush()
    return redirect('/virtual_escape_room')

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

def player_add(request): # url 'player/add'
    return HttpResponse("Player add")

def player_remove(request, player_id): # url 'player/remove/<int:player_id>'
    return HttpResponse(f"Player remove {player_id}")

def player_edit(request, player_id): # url 'player/edit/<int:player_id>'
    return HttpResponse(f"Player edit {player_id}")

def theme_add(request): # url 'theme/add'
    return HttpResponse("Theme add")

def theme_remove(request, theme_id): # url 'theme/remove/<int:theme_id>'
    return HttpResponse(f"Theme remove {theme_id}")

def theme_edit(request, theme_id): # url 'theme/edit/<int:theme_id>'
    return HttpResponse(f"Theme edit {theme_id}")

def puzzle_add(request): # url 'puzzle/add'
    return HttpResponse("Puzzle add")

def puzzle_remove(request, puzzle_id): # url 'puzzle/remove/<int:puzzle_id>'
    return HttpResponse(f"Puzzle remove {puzzle_id}")

def puzzle_edit(request, puzzle_id): # url 'puzzle/edit/<int:puzzle_id>'
    return HttpResponse(f"Puzzle edit {puzzle_id}")
