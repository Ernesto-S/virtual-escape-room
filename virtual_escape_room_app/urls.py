from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_virtual_escape_room),
    path('virtual_escape_room', views.show_landing_page),
    path('virtual_escape_room/login', views.login),
    path('virtual_escape_room/register', views.register),
    path('virtual_escape_room/logout', views.logout),
    path('get_data',views.get_data),
]
