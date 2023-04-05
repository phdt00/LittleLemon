from django.contrib import admin 
from django.urls import path 
from . import views
  
urlpatterns = [ 
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('menu/items/', views.MenuItemsView.as_view()),
    path('menu/items/<int:pk>', views.SingleMenuItemsView.as_view()),
]