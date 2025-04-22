from django.urls import path
from .views import create_order, print_label

urlpatterns = [
    path('', create_order, name='create_order'),
    path('print/<int:order_id>/', print_label, name='print_label')
]
