from django.db import models
from blog.models import Blog

class Basket(models.Model):
    name_order = models.CharField(max_length=100, default='Ivanov Ivan')
    choice_order = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name_order}:{self.choice_order}'