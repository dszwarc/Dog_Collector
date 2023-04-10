from django.shortcuts import render, HttpResponse

from .models import Dog
# Create your views here.
def home(request):
    return render(request, 'home.html')

def dog_index(request):
    dogs = Dog.models.get()
    return render(request, 'dogs/index.html', {'dogs': dogs})

def about(request):
    return render(request, 'about.html')

def dog_detail(request, dog_id):
    dog = Dog.models.get(id=dog_id)
    return render(request, 'dogs/details.html', {'dog':dog})