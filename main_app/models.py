from django.db import models
from django.urls import reverse

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})


# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def get_absolute_url(self):
        return reverse('dogs_detail', kwargs={'dog_id': self.id})
    
    def __str__(self):
        return f"{self.name}"

EXERCISES = (
    ('W', 'Went on walkies'),
    ('F', 'Played fetch'),
    ('H', 'Hiked'),
)

class Exercise(models.Model):
    date = models.DateField('exercise date')
    exercise = models.CharField(max_length=1, choices=EXERCISES, default=EXERCISES[0][0])
    how_long = models.IntegerField('how long (hours)')
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.get_exercise_display()} for {self.how_long} hour(s)."




