from django.shortcuts import render, redirect, HttpResponse
from virtual_escape_room_app.models import *

#all urls here are preappended with mythical_labyrinth_escape/
def show_puzzle(request, puzzle_id): # url 'puzzle/<int:puzzle_id>'
    context = {
        'puzzle': Puzzles.objects.get(id=puzzle_id)
    }
    return render(request, 'puzzle1.html', context)

def answer(request, puzzle_id): # url 'puzzle/<int:puzzle_id>/answer'
    answer = Puzzles.objects.get(answer=request.POST['answer'])
    return render(request, 'success_puzzle1.html')

def success_puzzle_1(request, id):
    puzzle = Puzzles.objects.get(id=3)
    return render(request, 'puzzle3.html')

def show_results(request): # url 'results'
    return HttpResponse("Show results")

def show_puzzle_2(request):
    return render(request, "templatePuzzle2.html")