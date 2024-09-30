from django.contrib import admin

# Register your models here.
# restaurant/admin.py
from .models import MenuItem, Table, Reservation, Inventory, Order, OrderItem

admin.site.register(MenuItem)
admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(Inventory)
admin.site.register(Order)
admin.site.register(OrderItem)
