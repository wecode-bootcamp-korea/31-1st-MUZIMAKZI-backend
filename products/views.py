from django.http import JsonResponse
from django.views import View

from .models import *

class ProductDetailView(View) :
    def get(self, request, product_id) :
        
            product            = Product.objects.get(id=product_id)
            image              = Image.objects.filter(product_id = product_id)
            
            detail_list = {
                'thumbnail_image_url' : product.thumbnail_image_url,
                'name'               : product.name,
                'price'              : product.price,
                'description'        : product.description,
                'size'               : [value.name for value in Size.objects.all()],
                'color'              : [value.name for value in Color.objects.all()],
                'image'              : [value.image_url for value in image]
               # 배송비, 태그
            }
                
            
            return JsonResponse({'message': detail_list}, status=200)
        

                
                
                            
            
            
            
            
        
        
        
        
        
        
        