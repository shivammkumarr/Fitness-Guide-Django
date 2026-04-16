from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('fat-loss/', views.fat_loss, name='fat_loss'),
    path('muscle-gain/', views.muscle_gain, name='muscle_gain'),
    path('weight-gain/', views.weight_gain, name='weight_gain'),
    path('exercises/', views.exercises, name='exercises'),
    path("supplements/", views.supplements, name="supplements"),

]
