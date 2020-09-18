from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_virtual_escape_room),
    path('virtual_escape_room', views.show_virtual_escape_room),
    path('virtual_escape_room/login', views.login),
    path('virtual_escape_room/register', views.register),
    path('virtual_escape_room/logout', views.logout),
    path('virtual_escape_room/pet_register', views.pet_register),
    path('virtual_escape_room/welcome', views.show_welcome),
    path('virtual_escape_room/request', views.request)
]