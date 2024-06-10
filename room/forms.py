# room/forms.py

from django import forms
from .models import Room
from .models import Message

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'slug']




class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
