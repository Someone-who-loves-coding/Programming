from django.contrib import admin
from django.urls import path,include
from HomePage import views

urlpatterns = [
    path('', views.Home , name='HomePage' )
]