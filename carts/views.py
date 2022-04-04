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
       
        option, created = ProductOption.objects.get_or_create(
            product = Product.objects.get(id= data['product_id']),
            size = Size.objects.get(id = data['size_id']),
            color = Color.objects.get(id = data['color_id']),
            
        )
        if not created :
            option.stock += int(data['quantity'])
        else:
            option.save()
        
        cart, created = Cart.objects.get_or_create(
            user = User.objects.get(id= data['user_id']),
            product_option = ProductOption.objects.get(id = option.id),
            quantity = data["quantity"]
        )
        if not created :
            cart.quantity += int(data['quantity'])
        else:
            cart.save()
            
        return JsonResponse({'message' : "SUCCESS" })
        
        
        
        
        
class CartListView(View) :
    
    def get(self, request) :
        data = json.loads(request.body)
        
        products = Cart.objects.filter(user_id = data['user_id'])
            
        if not products.exists() :
            return JsonResponse({'message' : 'Cart Is Empty'})
            
        return JsonResponse[{"message" : products.values('product_option')}]
        
       
       
       
        
        
        
        
        
        
        
        
        
            
            
        
            
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
            
            
            
        
        
        
        
        
        
            