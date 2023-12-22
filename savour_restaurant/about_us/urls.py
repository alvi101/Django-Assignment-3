from django.urls import path
from . import views

# About us URL
urlpatterns = [
    path("", views.about_us, name='about'),
]
