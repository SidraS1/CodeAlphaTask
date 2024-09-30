# restaurant/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('menu/add/', views.add_menu_item, name='add-menu-item'),
    path('menu/<int:pk>/update/', views.update_menu_item, name='update-menu-item'),
    path('reservation/make/', views.make_reservation, name='make-reservation'),
    path('order/place/', views.place_order, name='place-order'),
    path('inventory/<int:pk>/update/', views.update_inventory, name='update-inventory'),

]
# restaurant/urls.py
from django.urls import path
from .views import add_menu_item, menu_list  # Ensure you import your views

urlpatterns = [
    path('add-menu-item/', views.add_menu_item, name='add-menu-item'),
    path('menu-list/', views.menu_list, name='menu-list'),  # Add this line
    # ... other url patterns
]

