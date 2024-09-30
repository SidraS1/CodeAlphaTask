# Create your tests here.
# restaurant/tests.py
# restaurant/tests.py
from django.test import TestCase
from .models import MenuItem, Reservation, Order, Inventory, Table  # Ensure Table is imported
from django.urls import reverse
from .forms import MenuItemForm
from datetime import datetime

# MenuItem Model
class MenuItemTest(TestCase):
    def setUp(self):
        # Create a test menu item
        MenuItem.objects.create(name='Burger', description='Tasty beef burger', price=10.0, is_available=True)

    def test_menu_item_creation(self):
        # Get the menu item we just created
        burger = MenuItem.objects.get(name='Burger')
        self.assertEqual(burger.name, 'Burger')
        self.assertEqual(burger.price, 10.0)
        self.assertTrue(burger.is_available)

# Reservation Model
from django.utils import timezone
from .models import Reservation, Table

class ReservationTest(TestCase):
    def setUp(self):
        # Create a test table
        table = Table.objects.create(number=1, capacity=4)
        
        # Create a test reservation with a reservation time
        Reservation.objects.create(
            customer_name='John Doe',
            customer_contact='1234567890',
            table=table,
            reservation_time=timezone.now()  # Add a current time as reservation time
        )

    def test_reservation_creation(self):
        reservation = Reservation.objects.get(customer_name='John Doe')
        self.assertEqual(reservation.customer_contact, '1234567890')
        self.assertEqual(reservation.table.number, 1)  # Ensure it checks for Table instance


# Testing Views
class MenuItemViewTest(TestCase):
    def test_add_menu_item_view(self):
        # Test that the add menu item view loads correctly
        response = self.client.get(reverse('add-menu-item'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant/add_menu_item.html')

    def test_post_menu_item(self):
        # Test submitting the form via POST
        response = self.client.post(reverse('add-menu-item'), {
            'name': 'Pizza',
            'description': 'Delicious cheese pizza',
            'price': 12.5,
            'is_available': True
        })
        self.assertEqual(response.status_code, 302)  # Check for a redirect after form submission
        self.assertTrue(MenuItem.objects.filter(name='Pizza').exists())

# Testing Forms
class MenuItemFormTest(TestCase):
    def test_menu_item_form_valid(self):
        form_data = {'name': 'Salad', 'description': 'Fresh salad', 'price': 5.5, 'is_available': True}
        form = MenuItemForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_menu_item_form_invalid(self):
        form_data = {'name': '', 'description': 'Fresh salad', 'price': 5.5, 'is_available': True}
        form = MenuItemForm(data=form_data)
        self.assertFalse(form.is_valid())

