from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/', views.login, name='login'),
    path('email/', views.email, name='email'),
    path('compose/', views.compose, name='compose')
    
]
