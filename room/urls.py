# room/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('create/', views.create_room, name='create_room'),
    path('<slug:slug>/', views.room, name='room'),
    path('<slug:slug>/delete/', views.delete_room, name='delete_room'),
]
