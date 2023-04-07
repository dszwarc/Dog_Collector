from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dogs/', views.dog_index, name='dog_index'),   
]