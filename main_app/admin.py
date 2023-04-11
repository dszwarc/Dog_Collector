from django.contrib import admin

# Register your models here.
from .models import Dog, Exercise

admin.site.register(Dog)
admin.site.register(Exercise)