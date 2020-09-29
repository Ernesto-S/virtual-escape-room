from django.urls import path
from . import views

urlpatterns = [
    path('puzzle/<int:puzzle_id>', views.show_puzzle),
    path('puzzle/<int:puzzle_id>/answer', views.answer),
    path('results/<int:id>', views.show_results),
    path('update_game/<int:game_id>', views.update_game),
    path('test', views.show_test),
    path('timer', views.timer)
]

