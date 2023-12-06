from django.urls import path
from second_app.views import blog2

urlpatterns = [
      path('', blog2, name = 'blog2'),
]