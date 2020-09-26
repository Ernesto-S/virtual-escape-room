from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_virtual_escape_room),
    path('virtual_escape_room', views.show_landing_page),
    path('virtual_escape_room/login', views.login),
    path('virtual_escape_room/register', views.register),
    path('virtual_escape_room/logout', views.logout),
    path('get_data',views.get_data),
    path('player/add',views.player_add),
    path('player/remove/<int:player_id>',views.player_remove),
    path('player/edit/<int:player_id>',views.player_edit),
    path('theme/add',views.theme_add),
    path('theme/remove/<int:theme_id>',views.theme_remove),
    path('theme/edit/<int:theme_id>',views.theme_edit),
    path('puzzle/add',views.puzzle_add),
    path('puzzle/remove/<int:puzzle_id>',views.puzzle_remove),
    path('puzzle/edit/<int:puzzle_id>',views.puzzle_edit)
]
