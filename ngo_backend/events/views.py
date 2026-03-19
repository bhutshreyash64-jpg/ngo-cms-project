from django.shortcuts import render
from .models import Event
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

# Create your views here.
