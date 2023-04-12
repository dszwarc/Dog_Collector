from django.shortcuts import render, redirect
from .models import Dog, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, DetailView, ListView
from .forms import ExerciseForm
# Create your views here.

def assoc_toy(request, dog_id, toy_id):
    Dog.objects.get(id=dog_id).toys.add(toy_id)
    return redirect('dogs_detail', dog_id=dog_id)

def add_exercise(request, dog_id):
    form = ExerciseForm(request.POST)
    if form.is_valid():
        new_exercise = form.save(commit=False)
        new_exercise.dog_id = dog_id
        new_exercise.save()
    return redirect('dogs_detail', dog_id=dog_id)


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

class ToyList(ListView):
    model = Toy


class ToyDetail(DetailView):
    model = Toy


class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'


class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']


class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'