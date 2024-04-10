from django.shortcuts import render
from core.models import Notification
from django.http import HttpResponse

# Create your views here.


def index(request):
    if request.htmx:
        notification  = Notification.objects.get_or_create(name='Notification')[0]
        notification.count_not += 1
        notification.save()
        return HttpResponse('<p style="color: green; font-size: 16px;">message sent</p>')
    notification  = Notification.objects.get_or_create(name='Notification')[0]
    context = { 'num': notification.count_not }
    return render(request, 'index.html', context)