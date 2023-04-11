from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('dogs/', views.dog_index, name='dog_index'),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='dogs_detail'),
    path('dogs/create', views.DogCreate.as_view(), name='dogs_create'),
    path('dogs/<int:pk>/update', views.DogUpdate.as_view(), name='dogs_update'),
    path('dogs/<int:pk>/delete', views.DogDelete.as_view(), name='dogs_delete'),
    path('dogs/<int:dog_id>/add_exercise', views.add_exercise, name='add_exercise')
]

