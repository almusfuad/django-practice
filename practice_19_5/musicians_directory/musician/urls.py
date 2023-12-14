from django.urls import path
from . import views

urlpatterns = [
      path('add_musician/', views.AddMusicianView.as_view(), name = 'add_musician'),
]