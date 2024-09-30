# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Event, Registration
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_management/event_list.html', {'events': events})

# View event details
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_management/event_detail.html', {'event': event})

# Register for an event
@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        registration, created = Registration.objects.get_or_create(user=request.user, event=event)
        if created:
            return redirect('event_detail', event_id=event.id)
        else:
            return HttpResponse("You are already registered for this event.")
    return render(request, 'event_management/register_for_event.html', {'event': event})

# View user registrations
@login_required
def view_registrations(request):
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'event_management/view_registrations.html', {'registrations': registrations})

def home(request):
    return redirect('event_list')  # Redirect to event list