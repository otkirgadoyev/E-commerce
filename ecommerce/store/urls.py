from django.urls import path

from . import views

urlpatterns = [
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('updateItem/', views.updateItem, name='updateItem'),
    path('process_order/', views.processOrder, name='process_order')

]
