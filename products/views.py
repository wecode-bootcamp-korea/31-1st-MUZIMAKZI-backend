import json

from django.http import JsonResponse
from django.views import View

from products.models import Type, Product

class ProductCategoryView(View):
    def get(self, request, category_id):
        #try:
            types = Type.objects.filter(category=category_id)

            result = [{
                'name'         : type.name,
                'thumbnail_url':type.thumbnail_image_url
            } for type in types]

            return JsonResponse({'message': result}, status=200)

        # except KeyError:
        #     return JsonResponse({'message': 'invalid key'}, status=400)

class ProductListView(View):
    def get(self, request, type_id):
        #try:
            products = Product.objects.filter(type=type_id)

            result = [{
                'name'               : product.name,
                'price'              : product.price,
                'thumbnail_image_url': product.thumbnail_image_url
            } for product in products]

            return JsonResponse({'message': result}, status=200)

        # except KeyError:
        #     return JsonResponse({'message': 'invalid key'}, status=400)

