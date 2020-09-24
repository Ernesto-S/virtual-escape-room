from django.urls import path
from . import views

urlpatterns = [
    path('puzzle/<int:puzzle_id>', views.show_puzzle),
    path('puzzle/<int:puzzle_id>/answer', views.answer_puzzle_1),
    path('success_puzzle_1/<int:puzzle_id>', views.success_puzzle_1),
    path('results/<int:puzzle_id>', views.show_results),
]