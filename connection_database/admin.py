from django.contrib import admin
from connection_database.models import Car, StateNumberCar, ReviewCar, CategoryCar
# Register your models here.

admin.site.register(Car)
admin.site.register(StateNumberCar)
admin.site.register(ReviewCar)
admin.site.register(CategoryCar)
