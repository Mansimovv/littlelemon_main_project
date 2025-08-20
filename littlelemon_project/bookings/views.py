from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Booking
from datetime import datetime

# Create your views here.

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def bookings(request):
    if request.method=='POST':
        data = json.load(request)
        booking = Booking(
            first_name=data['first_name'],
            reservation_date=data['reservation_date'],
            reservation_slot=data['reservation_slot'],
        )
        booking.save()
        return render(request, 'bookings.html', {'message': 'Reservasiya uğurla əlavə edildi!'})
    

    elif request.method == 'GET':
        date_param = request.GET.get('date')
        if date_param:
            try:
                date_obj = datetime.strptime(date_param, '%Y-%m-%d').date()
                bookings = Booking.objects.filter(reservation_date=date_obj).values()
            except ValueError:
                bookings = []  # Tarix formatı yanlışdır
        else:
            bookings = Booking.objects.all().values()

        bookings_json = list(bookings)
        return render(request, 'bookings.html', {'bookings': bookings_json})
