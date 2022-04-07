import json

from django.http     import JsonResponse
from django.views    import View

from products.models import ProductOption
from products.models import *
from carts.models    import *
from users.models    import *

from users.utils     import login_decorator


class CartView(View) :
    @login_decorator
    def post(self, request):
        try :
            data = json.loads(request.body)
            user_id = request.user
            
            product_option     = ProductOption.objects.get(
                product        = Product.objects.get(id= data['product_id']),
                size           = Size.objects.get(id = data['size_id']),
                color          = Color.objects.get(id = data['color_id']),
            )

            cart, is_created   = Cart.objects.get_or_create(
                user           = User.objects.get(id = user_id),
                product_option = product_option,
                defaults       = {
                    "quantity" : data['quantity']
                }
            )

            if not is_created :
                cart.quantity += data['quantity']
                cart.save() 
                
            return JsonResponse({'message' : "SUCCESS" }, status=201)
        
        except KeyError :
             return JsonResponse({'message' : "KEY ERROR" }, status=400)
         
        
    @login_decorator
    def get(self, request) :
        try :
            user  = request.user
            carts = Cart.objects.filter(user = user)

            results = [{
                    "cart_id"       : cart.id,
                    "id"            : cart.product_option.product_id,
                    "thumbnail_url" : cart.product_option.product.thumbnail_image_url,
                    "name"          : cart.product_option.product.name,
                    'price'         : cart.product_option.product.price,
                    'size'          : cart.product_option.size.name,
                    'color'         : cart.product_option.color.name,
                    'quantity'      : cart.quantity
                
            } for cart in carts ]

            return JsonResponse({'message' : results}, status=200)
        
        except KeyError :
            return JsonResponse({'message' : "KEY ERROR"}, status=400)
        
  
    @login_decorator
    def put(self, request) :
        try :
            user     = request.user
            cart_id  = request.GET["cart_id"]
            quantity = request.GET['quantity']
            
            if not Cart.objects.filter(user = user).exists() :
                return JsonResponse({"message" : 'CART IS EMPTY'}, status = 400)
            
            if not Cart.objects.filter(id = cart_id).exists()   :
                return JsonResponse({"message" : 'NOT EXISTS ITEM IN CART'}, status = 400)
            
            update_carts = Cart.objects.get(user = user, id = cart_id)
            
            if update_carts.quantity == 0 :
                return JsonResponse({"message" : 'QUANTITY is INVALID'}, status = 200)
            
            else :   
                update_carts.quantity = quantity
                update_carts.save()
            
            return JsonResponse({'message' : "SUCCESS", "changed quantity" : update_carts.quantity}, status=201)
        
        except KeyError :
            return JsonResponse({'message' : 'KEY ERROR' }, status=400)
            
        
    @login_decorator   
    def delete(self, request) :
        try :
            user    = request.GET['user_id']
            cart_id = request.GET['cart_id']
            
            if not Cart.objects.filter(user = user).exists() :
                return JsonResponse({"message" : 'CART IS EMPTY'}, status = 400)
            
            if not Cart.objects.filter(id = cart_id) :
                return JsonResponse({"message" : 'NOT EXISTS ITEM IN CART'}, status = 400)
            
            delete_carts = Cart.objects.get(
                user  = user,
                id    = cart_id
            )
            
            delete_carts.delete()
            
            return JsonResponse({"message" : 'DELETED'}, status = 200)
        
        except KeyError:
            return JsonResponse({'message': "KEY ERROR"}, status=400)
       
