from django.contrib import admin 
from django.urls import path 
from . import views
  
urlpatterns = [ 
    path('', views.index, name='index'),
    path('items/', views.MenuItemsView.as_view()),
    path('items/<int:pk>', views.SingleMenuItemsView.as_view()),
]