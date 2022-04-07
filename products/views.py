from django.db.models import Q
from django.http        import JsonResponse
from django.views       import View

from products.models    import Type, Product, Category, Landing, Promote, Size, Color, Image

class LandingView(View):
    def get(self, request):
        categories    = Category.objects.all()
        landings      = Landing.objects.all()
        promotes      = Promote.objects.all()

        side_info=[{
            'category_id': category.id,
            'category_name': category.name,
            'types': [{
                'type_id' : type.id,
                'type_name': type.name
            } for type in category.type_set.all()]
        } for category in categories]

        landing_image = [{
            'landing_image_url': landing.image_url
        } for landing in landings]

        promotes = [{
            'promote_name': promote.name,
            'promote_image_url': promote.image_url
        } for promote in promotes]

        return JsonResponse({
            'side_info': side_info,
            'landings': landing_image,
            'promotes': promotes
        }, status=200)

class TypeView(View):
    def get(self, request, category_id):
        try:
            types = Type.objects.filter(category=category_id)

            results = [{
                'type_id'      : type.id,
                'name'         : type.name,
                'thumbnail_url': type.thumbnail_image_url
            } for type in types]

            return JsonResponse({'message': results}, status=200)

        except KeyError:
            return JsonResponse({'message': 'invalid key'}, status=400)

class ProductListView(View):
    def get(self, request):
        try:
            type_id         = request.GET.get('type_id')
            tags            = request.GET.getlist('tags', None)
            sort            = request.GET.get('sort', 'price')
            searching       = request.GET.get('name', None)
            limit           = int(request.GET.get('limit', 10))
            offset          = int(request.GET.get('offset', 0))

            condition = Q()

            if type_id:
                condition &= Q(type_id=type_id)
            if tags:
                condition &= Q(tagproduct__tag_id__in=tags)
            if searching:
                condition &= Q(name__icontains=searching)

            products = Product.objects.filter(condition).distinct().order_by(sort)[offset:offset+limit]

            results = [{
                'product_id'         : product.id,
                'thumbnail_image_url': product.thumbnail_image_url,
                'name'               : product.name,
                'price'              : product.price,
                'tags'               : [tags.tag.name for tags in product.tagproduct_set.all()]
            } for product in products]

            return JsonResponse({'message': results}, status=200)

        except Product.DoesNotExist:
            return JsonResponse({'message': 'product_not_exist'}, status=400)


class ProductDetailView(View) :
    
    def get(self, request, product_id) :
        try :
            product            = Product.objects.get(id = product_id)
            images             = product.image_set.all()
            
            result = {
                'thumbnail_image_url': product.thumbnail_image_url,
                'name'               : product.name,
                'price'              : product.price,
                'description'        : product.description,
                'size'               : [size.name for size in Size.objects.all()],
                'color'              : [color.name for color in Color.objects.all()],
                'image'              : [image.image_url for image in images ],
                'size_id'            : [size.id for size in Size.objects.all()],
                'color_id'           : [color.id for color in Color.objects.all()]
            }
            
            return JsonResponse({'message': result}, status=200)
    
        except Product.DoesNotExist:
            return JsonResponse({'message': "INVALID PRODUCT"}, status=400)
