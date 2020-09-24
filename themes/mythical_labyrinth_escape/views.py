from django.shortcuts import render, redirect, HttpResponse
from virtual_escape_room_app.models import *

#all urls here are preappended with mythical_labyrinth_escape/
def show_puzzle(request, puzzle_id): # url 'puzzle/<int:puzzle_id>'
    #puzzle_id = str(puzzle_id)
    #return HttpResponse(f"Show Puzzle {puzzle_id}")
    context = {
        'puzzle': Puzzles.objects.get(id=puzzle_id)
    }
    return render(request, 'puzzle1.html', context)

def answer_puzzle_1(request, puzzle_id): # url 'puzzle/<int:puzzle_id>/answer'
    #puzzle_id = str(puzzle_id)
    #return HttpResponse(f"Check answer{puzzle_id}")
    answer = Puzzles.objects.get(answer=request.POST['answer'])
    return render(request, 'success_puzzle1.html')

#def show_results(request, puzzle_id): # url 'results'
#    return HttpResponse("Show results")

