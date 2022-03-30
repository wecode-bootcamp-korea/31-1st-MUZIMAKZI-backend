import json

from django.http import JsonResponse
from django.views import View

from products.models import Type, Product


class ProductCategoryView(View):
    def get(self, request):
        try:
            data     = json.loads(request.body)
            category_id = data['category_id']

            types = Type.objects.filter(category=category_id)

            result = []
            for type in types:
                result.append({
                    'name'          : type.name,
                    'thumbnail_url' : type.thumbnail_image_url,
                })

            return JsonResponse({'message': result}, status=200)

        except KeyError:
            return JsonResponse({'message': 'invalid key'}, status=400)


class ProductListView(View):
    def get(self, request):
        try:
            data = json.loads(request.body)
            type_id = data['type_id']

            products = Product.objects.filter(type=type_id)

            result = []
            for product in products:
                result.append({
                    'name': product.name,
                    'price': product.price,
                    'thumbnail_image_url': product.thumbnail_image_url
                })

            return JsonResponse({'message': result}, status=200)
        except KeyError:
            return JsonResponse({'message': 'invalid key'}, status=400)
