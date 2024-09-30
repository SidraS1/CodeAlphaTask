# Create your views here.

# restaurant/views.py
from django.shortcuts import render, redirect
from .forms import MenuItemForm
from .models import MenuItem

# View for creating a new menu item
def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu-list')  # Redirect to menu listing
    else:
        form = MenuItemForm()
    return render(request, 'restaurant/add_menu_item.html', {'form': form})

# View for updating an existing menu item
def update_menu_item(request, pk):
    menu_item = MenuItem.objects.get(pk=pk)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('menu-list')
    else:
        form = MenuItemForm(instance=menu_item)
    return render(request, 'restaurant/update_menu_item.html', {'form': form})

# View for Making Reservations
from .forms import ReservationForm
from .models import Reservation

# View for creating a reservation
def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation-list')
    else:
        form = ReservationForm()
    return render(request, 'restaurant/make_reservation.html', {'form': form})

# View for Placing Orders
from .forms import OrderForm
from .models import Order

# View for creating an order
def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order-list')
    else:
        form = OrderForm()
    return render(request, 'restaurant/place_order.html', {'form': form})

# View for Updating Inventory
from .forms import InventoryForm
from .models import Inventory

# View for updating inventory
def update_inventory(request, pk):
    inventory_item = Inventory.objects.get(pk=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory_item)
        if form.is_valid():
            form.save()
            return redirect('inventory-list')
    else:
        form = InventoryForm(instance=inventory_item)
    return render(request, 'restaurant/update_inventory.html', {'form': form})

# restaurant/views.py
from django.shortcuts import render
from .models import MenuItem

def menu_list(request):
    # Retrieve all menu items from the database
    menu_items = MenuItem.objects.all()
    return render(request, 'restaurant/menu_list.html', {'menu_items': menu_items})
