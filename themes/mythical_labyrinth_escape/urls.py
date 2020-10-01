from django.urls import path
from . import views

urlpatterns = [
    path('puzzle/<int:puzzle_id>', views.show_puzzle),
    path('puzzle/<int:puzzle_id>/answer', views.answer),
<<<<<<< HEAD
    path('results', views.show_results),
    path('puzzle_3', views.puzzle_3),
    path('check_3_answer', views.check_3_answer),
    path('puzzle_3_solution', views.puzzle_3_solution),
]
=======
    path('results/<int:id>', views.show_results),
    path('update_game/<int:game_id>', views.update_game),
    path('test', views.show_test),
    path('timer', views.timer)
]

>>>>>>> origin/master
