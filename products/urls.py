from django.urls import path

from products.views import ProductCategoryView, ProductListView

urlpatterns = [
    path('/categories', ProductCategoryView.as_view()),
    path('/categories/list', ProductListView.as_view())
]
