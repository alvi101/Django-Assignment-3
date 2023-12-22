from django.urls import path
from . import views

# Meal URL
urlpatterns = [
    path("", views.meal, name='meal'),
]
