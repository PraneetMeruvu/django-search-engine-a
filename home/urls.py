from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    
    path('', views.upload_files, name='upload_files'),
    path('search/', views.search_files, name='search_files'),
]
