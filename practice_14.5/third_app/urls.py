from django.urls import path
from third_app.views import blog3

urlpatterns = [
      path('', blog3, name = 'blog3'),
]