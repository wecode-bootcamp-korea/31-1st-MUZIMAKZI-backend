from django.urls import path

from .views import CartView


urlpatterns = [
    # :8000/carts
    path('', CartView.as_view()),
]
