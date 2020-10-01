from django.shortcuts import render, redirect, HttpResponse
from virtual_escape_room_app.models import *
from django.db.models import Q 

#all urls here are preappended with mythical_labyrinth_escape/
def show_puzzle(request, puzzle_id):
    context = {
        'puzzle': Puzzle.objects.get(id=puzzle_id)
    }
    return render(request, f'puzzle{puzzle_id}.html', context)

def answer(request, puzzle_id): # url 'puzzle/<int:puzzle_id>/answer'
    if request.method == "POST":
        puzzle = Puzzle.objects.get(id=puzzle_id)
        if puzzle.answer == request.POST['answer']:
            return render(request, f'success_puzzle{puzzle_id}.html')
        else:
            return redirect(f'/mythical_labyrinth_escape/puzzle/{puzzle_id}')
    return redirect('/virtual_escape_room')

def show_results(request,id): # url 'results'
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

def show_test(request):
    return render(request, 'templatePuzzle2.html')

def update_game(request, game_id):
    player_id = request.session['player_id']
    edit_game = Game.objects.get(id = game_id)
    edit_game.timer = request.session['timer']
    edit_game.status = 'Success'
    edit_game.save()
    return redirect(f'/mythical_labyrinth_escape/results/{player_id}')


def timer(request):
    request.session['timer'] = request.session['timer'] - 1
    request.session.save()
    return request.session['timer']
