# Create your models here.
# restaurant/models.py
# MenuItem Model.
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Table Model.
from django.db import models

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.number}"
# Reservation Model
class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_contact = models.CharField(max_length=15)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)  # Add this line if you want to keep notes

    def __str__(self):
        return f"Reservation for {self.customer_name} at {self.reservation_time}"


# Inventory Model.
class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=20)

    def __str__(self):
        return self.item_name

# Order Model.
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    items = models.ManyToManyField(MenuItem, through='OrderItem')
    order_time = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.customer_name}"

# OrderItem Model(Intermediate Model).
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} for Order {self.order.id}"

