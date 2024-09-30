# restaurant/forms.py
from django import forms
from .models import MenuItem, Reservation, Order, Inventory

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'is_available']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer_name', 'customer_contact', 'table', 'reservation_time', 'notes']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'items', 'total_amount']

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['item_name', 'quantity', 'unit']

