from django.shortcuts import render

# Create your views here.
from django.views import View

from apps.cars.models import Car


class CarList(View):
    def get(self, request, car_id=None, car_dealer=None):
        cars = Car.objects.filter(dealer__id=car_dealer)
        if car_id:
            car = Car.objects.get(id=car_id)
            return render(request, 'car_information.html', {'car': car})
        return render(request, 'base.html', {'cars':cars})
