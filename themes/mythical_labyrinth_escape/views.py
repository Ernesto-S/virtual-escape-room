from django.shortcuts import render, redirect, HttpResponse
from virtual_escape_room_app.models import *

#all urls here are preappended with mythical_labyrinth_escape/
def show_puzzle(request): # url 'puzzle/<int:puzzle_id>'
    context = {
        'puzzle': Puzzles.objects.get(pk=1)
    }
    return render(request, 'puzzle1.html', context)

def answer(request, puzzle_id): # url 'puzzle/<int:puzzle_id>/answer'
    answer = Puzzles.objects.get(answer=request.POST['answer'])
    return render(request, 'success_puzzle1.html')

def show_puzzle_2(request):
    context = {
        'puzzle_2': Puzzles.objects.get(pk=2)
    }
    return render(request, "puzzle2.html", context)

def answer_2(request): # url 'puzzle/<int:puzzle_id>/answer'
    answer = Puzzles.objects.get(pk=2, answer=request.POST['answer'])
    return render(request, 'success_puzzle2.html')

def show_puzzle_3(request):
    context = {
        'this_puzzle': Puzzles.objects.get(pk=3)
    }
    return render(request, 'puzzle3.html', context)

def answer_3(request): # url 'puzzle/<int:puzzle_id>/answer'
    answer = Puzzles.objects.get(pk=3, answer=request.POST['answer'])
    return render(request, 'success_puzzle3.html')

def show_results(request,id): # url 'results'
    # if 'usrname' not in request.session:
    #     return redirect('/')
    qryPlayer=Player.objects.get(id=id)
    qryGames= Game.objects.order_by('timer')
    qryPlayerUserName=qryPlayer.username
    print(qryPlayerUserName)
    if qryPlayer !='':
        qryAchievements=qryGames.filter(Q(player__username__exact=qryPlayerUserName) & Q(status__exact='Success'))
        qryleader=qryThemes.filter(status__exact='Success')
        context={
            'queryachievements':qryAchievements,
            'queryleaderboard':qryleader
        }   
        print(qryAchievements)
        print(qryThemes)
        return render(request, "results.html",context)

