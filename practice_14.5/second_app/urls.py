from django.urls import path
from second.views import home

urlpatterns = [
      path('', home, name = 'home'),
]