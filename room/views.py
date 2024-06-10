# room/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Room, Message
from .forms import RoomForm
from .forms import MessageForm

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})

# room/views.py



@login_required
def room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    messages = room.messages.all()[:25]  # Retrieve messages for the room
    user = request.user
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.room = room
            message.save()
            return redirect('room', slug=slug)
    else:
        form = MessageForm()
    return render(request, 'room/room.html', {'room': room, 'messages': messages, 'user': user, 'form': form})


@login_required
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms')
    else:
        form = RoomForm()
    return render(request, 'room/create_room.html', {'form': form})

@login_required
def delete_room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    if request.method == 'POST':
        room.delete()
        return redirect('rooms')
    return render(request, 'room/delete_room.html', {'room': room})
