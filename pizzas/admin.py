from django.contrib import admin

# Register your models here.
from pizzas.models import Pizza

admin.site.register(Pizza)