from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dogs/', views.dog_index, name='dog_index', {dogs: dogs}),   
]

class Dog:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Appa', 'corgi', 'The goodest little boi', 5),
  Dog('Kropka', 'beagle', 'My first dog <3', 18),
  Dog('Chip', 'unknown mix', "Appa's least favorite cousin.", 4)
]