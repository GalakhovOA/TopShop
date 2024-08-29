from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('1', views.home_page, name='home_page'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]

