from django.urls import path
from .views import *


urlpatterns = [
    path('/add_cart', AddCartView.as_view() ),
    path('/cart_list', CartListView.as_view())
    
]
