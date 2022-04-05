import json

from django.http  import JsonResponse
from django.views import View

from products.models import ProductOption
from users.utils     import login_decorator
from products.models import *
from .models         import *
from users.models    import *

class CartView(View) :
    def post(self, request):
        data = json.loads(request.body)

        quantity = data['quantity']
       
        product_option = ProductOption.objects.get(
            product = Product.objects.get(id= data['product_id']),
            size    = Size.objects.get(id = data['size_id']),
            color   = Color.objects.get(id = data['color_id']),
        )

        cart, is_created = Cart.objects.get_or_create(
            user           = request.user,
            product_option = product_option,
            defaults       = {
                "quantity" : quantity
            }
        )

        if not is_created:
            cart.quantity += quantity
            
        return JsonResponse({'message' : "SUCCESS" }, status=201)
    
    # GET :8000/carts?category=a
    def get(self, request) :
        data = json.loads(request.body)

        carts = Cart.objects.filter(user = request.user)

        results = [{
            "cart_id" : cart.id,
            "product" : {
                "id"           : cart.product_option.product_id,
                "thumbnail_url": cart.product_option.product.thumbnail_url
            }
        } for cart in carts ]

        return JsonResponse({'message' : results}, status=200)        