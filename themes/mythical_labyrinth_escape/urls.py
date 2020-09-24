from django.urls import path
from . import views

urlpatterns = [
    path('puzzle/<int:puzzle_id>', views.show_puzzle),
    path('puzzle/<int:puzzle_id>/answer', views.answer),
    path('results', views.show_results),
    path('puzzle_3', views.puzzle_3),
    path('check_3_answer', views.check_3_answer),
    path('puzzle_3_solution', views.puzzle_3_solution),
]