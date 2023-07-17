from django.shortcuts import render, get_object_or_404
from . models import Car

# Create your views here.

def cars(request):
    car = Car.objects.order_by('-created_date')
    return render(request,'cars/cars.html', locals())

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    return render(request, 'cars/car_detail.html', locals())
