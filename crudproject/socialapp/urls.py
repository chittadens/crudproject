from django.urls import path
from .import views

urlpatterns = [
  path('signup/', views.signup,name="signup"),
  path('signuptable/', views.signuptable,name="signuptable"), 
  path('login/', views.login,name="login"),

]