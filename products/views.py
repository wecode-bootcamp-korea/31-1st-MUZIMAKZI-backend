from django.http import JsonResponse
from django.views import View

from .models import *

class ProductDetailView(View) :
    def get(self, request, product_id) :
        product            = Product.objects.get(id=product_id)
        
        result = {
            'thumbnail_image_url': product.thumbnail_image_url,
            'name'               : product.name,
            'price'              : product.price,
            'description'        : product.description,
            'size'               : [value.name for value in Size.objects.all()],
            'color'              : [value.name for value in Color.objects.all()],
            'image'              : [ image.url for image in product.image_set.all() ]
        }
        
        return JsonResponse({'message': result}, status=200)