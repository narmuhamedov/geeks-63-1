from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CategoryCar(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    title = models.CharField(max_length=100)
    person = models.CharField(max_length=100, default='Ivanov Ivan')
    categories = models.ManyToManyField(CategoryCar, null=True, blank=True)

    def __str__(self):
        return f'{self.title}---{', '.join(i.name for i in self.categories.all())}'

    # def __str__(self):
    #     return self.title


class StateNumberCar(models.Model):
    car_title = models.OneToOneField(Car, on_delete=models.CASCADE)
    nummer_car = models.CharField(max_length=10, default='0_KG_')

    def __str__(self):
        return self.nummer_car

class ReviewCar(models.Model):
    choice_car = models.ForeignKey(Car, on_delete=models.CASCADE, 
                                   related_name='review')
    mark = models.PositiveIntegerField(validators=[MinValueValidator(1), 
                                                   MaxValueValidator(5)])
    text = models.TextField()


    def __str__(self):
        return f'{self.choice_car}----{self.mark}'

