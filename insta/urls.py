from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.image, name='image'),
    path('instagram/', views.instagram, name='instagram'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]