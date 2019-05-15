from django import forms
from .models import CreateRoom

class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = CreateRoom
        fields = ("creator", "create_list",)