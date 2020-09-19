from django.shortcuts import render, redirect, HttpResponse

#all urls here are preappended with mythical_labyrinth_escape/
def show_puzzle(request, puzzle_id): # url 'puzzle/<int:puzzle_id>'
    puzzle_id = str(puzzle_id)
    return HttpResponse(f"Show Puzzle {puzzle_id}")

def answer(request, puzzle_id): # url 'puzzle/<int:puzzle_id>/answer'
    puzzle_id = str(puzzle_id)
    return HttpResponse(f"Check answer{puzzle_id}")

def show_results(request): # url 'results'
    return HttpResponse("Show results")
