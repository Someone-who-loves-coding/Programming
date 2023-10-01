from django.contrib import admin
from django.urls import path,include
from HomePage import views

urlpatterns = [
    path('', views.Home , name='HomePage' ),
    path('About/', views.About , name='About' ),
    path('Contact/', views.Contact_Us , name='Contact' )
]