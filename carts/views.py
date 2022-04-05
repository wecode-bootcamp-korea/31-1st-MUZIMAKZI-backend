from itertools import product
from django.http import JsonResponse
from django.views import View

from products.models import ProductOption
from users.utils import login_decorator
from products.models import *
from .models import *
from users.models import *
import json


class AddCartView(View) :
   
    def post(self, request):
        data = json.loads(request.body)
        
        #user_id = request.user.id
        user_id = data['user_id']
       
        option = ProductOption.objects.create(
            product = Product.objects.get(id= data['product_id']),
            size = Size.objects.get(id = data['size_id']),
            color = Color.objects.get(id = data['color_id']),
            stock = int(data['quantity'])
            
        )
        
        
       
        Cart.objects.create(
            user = User.objects.get(id= data['user_id']),
            product_option = ProductOption.objects.get(id = option.id),
            quantity = option.stock
        )
        
            
        return JsonResponse({'message' : "SUCCESS" })
        
        
        
        
        
class CartListView(View) :
    
    def get(self, request) :
        data = json.loads(request.body)
        
        products = Cart.objects.filter(user_id = data['user_id'])
        
    
        
        if not products.exists() :
            return JsonResponse({'message' : 'Cart Is Empty'})
        
        result = [{
            "thumbnail_url" : Product.objects.get(id = ProductOption.objects.get(id=product.product_option_id).product_id).thumbnail_image_url,
            "name"          : Product.objects.get(id = ProductOption.objects.get(id=product.product_option_id).product_id).name,
            "price"         : Product.objects.get(id = ProductOption.objects.get(id=product.product_option_id).product_id).price,
            "color"         : Color.objects.get(id = ProductOption.objects.get(id=product.product_option_id).color_id).name,
            "size"          : Size.objects.get(id =ProductOption.objects.get(id=product.product_option_id).size_id).name,
            #"quantity"      : Cart.objects.get(product_option_id = product.product_option_id).quantuty,
        } for product in products]
        
        
        return JsonResponse({'message' : result})        
        
        
        
        
        
        
        
        
        
        
            
        
    
    

        
       
       
       
        
        
        
        
        
        
        
        
        
            
            
        
            
        #Cart.objects.create(
         #   user = data['user_id'],
          #  product_optinon = data['product_option_id'],
           # quantuty = data['quantuty'],
         
        
        
       
        
        
        #user = User.objects.get(id = user_id)
     
        
        
        
        
        
        
        
      #  if ProductOption.objects.filter(
       #     
        #    product_id = data['product_id'],
          #  size = data['size_id'],
         #   color = data['color_id']
            
            
            
        
        
        
        
        
        
            