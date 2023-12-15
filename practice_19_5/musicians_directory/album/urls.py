from django.urls import path
from . import views

urlpatterns = [
      path('add_album/', views.AlbumCreateView.as_view(), name = 'add_album'),
      path('edit_album/<int:pk>', views.AlbumUpdateView.as_view(), name = 'edit_album'),
      path('delete_album/<int:pk>', views.AlbumDeleteView.as_view(), name = 'delete_album'),
]