from django.urls import path
from . import views

urlpatterns = [
      path('add_album/', views.AlbumCreateView.as_view(), name = 'add_album'),
]