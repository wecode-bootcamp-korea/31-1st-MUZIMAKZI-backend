from django.urls import path

from products.views import TypeView, ProductListView, LandingView, ProductDetailView

urlpatterns = [
    path('/categories/<int:category_id>/types', TypeView.as_view()),
    path('/categories', ProductListView.as_view()),
    path('', LandingView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view())
]