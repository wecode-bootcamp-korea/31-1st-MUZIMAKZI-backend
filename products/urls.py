from django.urls import path

from products.views import TypeView, ProductListView, LandingView

urlpatterns = [
    # :8000/products/cateogories/1/type
    path('/categories/<int:category_id>/type`', TypeView.as_view()),
    path('/categories', ProductListView.as_view()),
    path('', LandingView.as_view()),
]
