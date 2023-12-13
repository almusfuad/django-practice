from django.urls import path
from . import views


urlpatterns = [
      path('', views.home, name = 'home'),
      path('registration/', views.signup, name = 'signup'),
      path('login/', views.user_login, name = 'login'),
      path('profile/', views.profile, name = 'profile'),
      path('logout/', views.user_logout, name = 'logout'),
      path('update_password/', views.update_user_pass, name = 'update_password'),
      path('set_password/', views.set_user_pass, name = 'set_password'),
]