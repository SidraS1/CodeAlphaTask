from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),  # Add this for listing events
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/register/', views.register_for_event, name='register_for_event'),
    path('my-registrations/', views.view_registrations, name='view_registrations'),
]

