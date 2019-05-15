from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import CreateRoom
from .forms import CreateRoomForm
from django.http import HttpResponse


@login_required(login_url='/account/login')
@csrf_exempt
def create_notice(request):
    return render(request, "create\create_notice.html")

@login_required(login_url='/account/login')
@csrf_exempt
def create_room(request):
    # if request.method == "POST":
    #     createroom_form = CreateRoomForm(data=request.POST)
    #     if createroom_form.is_valid():
    #         new_createroom = createroom_form.save(commit=False)
    #         new_createroom.save()
    # else:
    #     createroom_form = CreateRoomForm
    return render(request, "create/create_room.html")   #, {"createroom_form": createroom_form}

def technology_column(request):
    return render(request, "create/technology/technology-column.html")

def technology_others(request):
    return render(request, "create/technology/technology-others.html")

def technology_navigation(request):
    return render(request, "create/technology/technology-navigation.html")

def speech_recognition(request):
    return render(request, "create/technology/speech-recognition.html")

def visual_processing(request):
    return render(request, "create/technology/visual-processing.html")

def big_data(request):
    return render(request, "create/technology/big-data.html")

def clound_computing(request):
    return render(request, "create/technology/clound-computing.html")

def visual_navigation(request):
    return render(request, "create/technology/visual-navigation.html")

def radar_navigation(request):
    return render(request, "create/technology/radar-navigation.html")

def brand(request):
    return render(request, "create/brand.html")

