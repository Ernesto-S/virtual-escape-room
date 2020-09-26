from django.urls import path
from . import views

urlpatterns = [
    path('puzzle/1', views.show_puzzle),
    path('puzzle/<int:puzzle_id>/answer', views.answer),
    path('puzzle/2', views.show_puzzle_2),
    #path('success_puzzle_1', views.success_puzzle_1),
    path('puzzle/3', views.show_puzzle_3),
    path('puzzle/2/answer_2', views.answer_2),
    path('puzzle/3/answer_3', views.answer_3),
    path('results', views.show_results),
]