from django.shortcuts import render
from connection_database.models import Car

def car_list_view(request):
    if request.method == 'GET':
        car = Car.objects.all().order_by('-id')
        return render(
            request,
            'car_list.html',
            {
                'car': car
            }
        )
