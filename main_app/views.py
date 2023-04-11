from django.shortcuts import render
from .models import Dog
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ExerciseForm
# Create your views here.

def add_exercise(request):
    pass

def home(request):
    return render(request, 'home.html')

def dog_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})

def about(request):
    return render(request, 'about.html')

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    exercise_form = ExerciseForm()
    return render(request, 'dogs/detail.html', {'dog':dog, 'form': exercise_form})
    
    


class DogCreate(CreateView):
    model = Dog
    fields = '__all__'

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'