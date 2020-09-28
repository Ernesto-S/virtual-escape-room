from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
from django.db.models import Q
import bcrypt
import pytz
import datetime


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
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
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
    qry_puzzles=Puzzle.objects.all()
    qry_games=Game.objects.all()
    context={
            'queryplayers':qry_players,
            'querythemes':qry_themes,
            'querypuzzles':qry_puzzles,
            'querygames':qry_games
        }   
    return render(request, "get_data.html", context)

def results(request,id):
    # if 'usrname' not in request.session:
    #     return redirect('/')
    qryPlayer=Player.objects.get(id=id)
    qryGames= Game.objects.order_by('timer')
    qryPlayerUserName=qryPlayer.username
    print(qryPlayerUserName)
    if qryPlayer !='':
        qryAchievements=qryGames.filter(Q(players__username__exact=qryPlayerUserName) & Q(status__exact='Success'))
        qryleader=qryGames.filter(status__exact='Success')
        context={
            'queryachievements':qryAchievements,
            'queryleaderboard':qryleader
        }   
        print(qryAchievements)
        print(qryGames)
        return render(request, "results.html",context)
        
def player_add(request): # url 'player/add'
    if request.method == 'POST':
        errors = Player.objects.player_validator(request.POST)
        if len(errors) > 0:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/get_data')
        else:
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            new_player = Player.objects.create(
                username=request.POST['username'],
                email=request.POST['email'],
                password=hashed_pw
            )
            return redirect('/get_data')
    return redirect('/get_data')

def player_remove(request, player_id): # url 'player/remove/<int:player_id>'
    player_removing = Player.objects.get(id=player_id)
    player_removing.delete()
    return redirect('/get_data')

def player_edit(request, player_id): # url 'player/edit/<int:player_id>'
    return HttpResponse(f"Player edit {player_id}")

def theme_add(request): # url 'theme/add'
    if request.method == 'POST':
        errors = Theme.objects.theme_validator(request.POST)
        if len(errors) > 0:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/get_data')
        else:
            new_theme = Theme.objects.create(
                title=request.POST['title'],
                description=request.POST['description']
            )
            return redirect('/get_data')
    return redirect('/get_data')

def theme_remove(request, theme_id): # url 'theme/remove/<int:theme_id>'
    theme_removing = Theme.objects.get(id=theme_id)
    theme_removing.delete()
    return redirect('/get_data')

def theme_edit(request, theme_id): # url 'theme/edit/<int:theme_id>'
    return HttpResponse(f"Theme edit {theme_id}")

def puzzle_add(request): # url 'puzzle/add'
    if request.method == 'POST':
        new_Puzzle = Puzzle.objects.create(
            theme=Theme.objects.get(id=request.POST['theme_id']),
            question=request.POST['question'],
            hint=request.POST['hint'],
            story=request.POST['story'],
            answer=request.POST['answer']
        )
        return redirect('/get_data')
    return redirect('/get_data')

def puzzle_remove(request, puzzle_id): # url 'puzzle/remove/<int:puzzle_id>'
    puzzle_removing = Puzzle.objects.get(id=puzzle_id   )
    puzzle_removing.delete()
    return redirect('/get_data')

def puzzle_edit(request, puzzle_id): # url 'puzzle/edit/<int:puzzle_id>'
    return HttpResponse(f"Puzzle edit {puzzle_id}")

def game_add(request): # url 'game/add'
    if request.method == 'POST':
        new_Game = Game.objects.create(
            players=Player.objects.get(id=request.POST['player_id']),
            theme=Theme.objects.get(id=request.POST['theme_id']),
            status=request.POST['status'],
            timer=request.POST['timer']
        )
        return redirect('/get_data')
    return redirect('/get_data')

def game_remove(request, game_id): # url 'game/remove/<int:game_id>'
    game_removing = Game.objects.get(id=game_id   )
    game_removing.delete()
    return redirect('/get_data')

def game_edit(request, game_id): # url 'game/edit/<int:game_id>'
    return HttpResponse(f"Game edit {game_id}")

def create_game(request):
    playerid=request.session['player_id']
    new_game=Game.objects.create(players=Player.objects.get(id=playerid),theme=Theme.objects.get(id="1"),status="In Progress",timer=10)
    request.session['timer']=new_game.timer
    request.session['game_id']=new_game.id
    return redirect('/mythical_labyrinth_escape/puzzle/1')

