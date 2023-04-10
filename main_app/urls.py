from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('dogs/', views.dog_index, name='dog_index'),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='dogs_detail')   
]

