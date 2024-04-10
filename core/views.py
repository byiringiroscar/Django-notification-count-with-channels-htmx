from django.shortcuts import render
from core.models import Notification

# Create your views here.


def index(request):
    if request.htmx:
        notification  = Notification.objects.get_or_create(name='Notification')[0]
        notification.count_not += 1
        notification.save()
        context = { 'num': notification.count_not }
        return render(request, 'partials/notification_counter.html', context)
    notification  = Notification.objects.get_or_create(name='Notification')[0]
    context = { 'num': notification.count_not }
    return render(request, 'index.html', context)