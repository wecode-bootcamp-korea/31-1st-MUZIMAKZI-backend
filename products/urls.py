from django.urls import path, include

from products.views import ProductCategoryView

urlpatterns = [
    path('/categories', ProductCategoryView.as_view()),
]
