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

# dogs = [
#   Dog('Appa', 'Corgi', 'The goodest little boi', 5),
#   Dog('Kropka', 'Beagle', 'My first dog <3', 18),
#   Dog('Chip', 'Unknown mix', "Appa's least favorite cousin.", 4),
#   Dog('Momo', 'Dachshund', "Appa's brother/sister that he doesn't know about.", 0)
# ]