from django.urls import path, include
from . import views


urlpatterns = [
    path('geeksfor/', views.geeksfor),
    path('earthly/', views.earthly),
]