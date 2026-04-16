from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def fat_loss(request):
    return render(request, "fat_loss.html")

def muscle_gain(request):
    return render(request, "muscle_gain.html")

def weight_gain(request):
    return render(request, "weight_gain.html")

def exercises(request):
    return render(request, "exercises.html")    

def supplements(request):
    return render(request, "supplements.html")