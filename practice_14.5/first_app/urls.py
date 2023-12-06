from django.urls import path
from first_app.views import blog1

urlpatterns = [
      path('', blog1, name = 'blog1'),
]