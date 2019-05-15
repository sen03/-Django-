from django.urls import path, re_path
from . import views

app_name = "create"

urlpatterns = [
    path('create-notice/', views.create_notice, name="create_notice"),
    path('create-room/', views.create_room, name="create_room"),

    path('technology-column/', views.technology_column, name="technology_column"),
    path('technology-column/technology-navigation.html', views.technology_navigation, name="technology_navigation"),
    path('technology-column/technology-navigation.html', views.technology_navigation, name="technology_navigation"),
    path('technology-column/technology-navigation.html', views.technology_navigation, name="technology_navigation"),
    path('technology-column/speech-recognition.html', views.speech_recognition, name="speech_recognition"),
    path('technology-column/visual-processing.html', views.visual_processing, name="visual_processing"),
    path('technology-column/big-data.html', views.big_data, name="big_data"),
    path('technology-column/clound-computing.html', views.clound_computing, name="clound_computing"),
    path('technology-column/visual-navigation.html', views.visual_navigation, name="visual_navigation"),
    path('technology-column/radar-navigation.html', views.radar_navigation, name="radar_navigation"),
    path('technology-column/technology-others.html', views.technology_others, name="technology_others"),

    path('brand/', views.brand, name="brand"),
]