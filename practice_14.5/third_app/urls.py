from django.urls import path
from third_app.views import home

urlpatterns = [
      path('', home, name = 'home'),
]