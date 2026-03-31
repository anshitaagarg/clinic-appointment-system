from django.shortcuts import render
from .models import Appointment, Token
from django.db.models import Count
from datetime import date

def queue_display(request):
    tokens = Token.objects.all().order_by('token_number')
    return render(request, 'clinic/queue.html', {'tokens': tokens})

def reports(request):
    # Daily report
    today = date.today()
    daily_count = Appointment.objects.filter(
        schedule__date=today
    ).count()

    # Doctor-wise report
    doctor_report = Appointment.objects.values(
        'doctor__name'
    ).annotate(total=Count('id'))

    return render(request, 'clinic/reports.html', {
        'daily_count': daily_count,
        'doctor_report': doctor_report
    })