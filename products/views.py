import json

from django.http import JsonResponse
from django.views import View

from products.models import Type


class ProductCategoryView(View):
    def get(self, request):
        try:
            data     = json.loads(request.body)
            category = data['category_id']

            types = Type.objects.filter(category=category)

            result=[]
            for type in types:
                result.append({
                    'name'          : type.name,
                    'thumbnail_url' : type.thumbnail_image_url,
                })

            return JsonResponse({'message': result}, status=200)

        except KeyError:
            return JsonResponse({'message': 'invalid key'}, status=400)


    def post(self, request):
        pass
