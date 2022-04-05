from django.urls import path

from products.views import TypeView, ProductListView, LandingView

urlpatterns = [
    path('/categories/<int:category_id>', TypeView.as_view()),
    path('/categories', ProductListView.as_view()),
    path('', LandingView.as_view()),
]
