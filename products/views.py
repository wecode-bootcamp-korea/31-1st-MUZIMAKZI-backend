from django.db.models import Q, Count
from products.models import Type, Product, Tag, TagProduct

from django.http import JsonResponse
from django.views import View


class LandingView(View):
    def get(self, request):
        return JsonResponse({'message': 'here'},status=200)



class ProductCategoryView(View):
    def get(self, request, category_id):
        try:
            types = Type.objects.filter(category=category_id)

            result = [{
                'name'         : type.name,
                'thumbnail_url':type.thumbnail_image_url
            } for type in types]

            return JsonResponse({'message': result}, status=200)

        except KeyError:
            return JsonResponse({'message': 'invalid key'}, status=400)

class ProductListView(View):
    def get(self, request):
        try:
            type_id         = request.GET.get('type_id')
            tags            = request.GET.getlist('tags', None)
            sort            = request.GET.get('sort', 'asc')
            searching       = request.GET.get('name')
            limit           = int(request.GET.get('limit', 10))
            offset          = int(request.GET.get('offset', 0))

            sort_option = {
                'id'  : 'id',
                'asc': 'price',
                'desc': '-price'
            }

            condition = Q()
            if tags:
                condition &= Q(tag_id__in=tags)

            products_key = TagProduct.objects.values('product_id').annotate(tag_count=Count('tag_id'))\
                .filter(condition).filter(tag_count__gte=len(tags))

            products = Product.objects.filter(id__in=[row['product_id'] for row in products_key[:]])\
                           .filter(Q(name=searching) | Q(type_id=type_id))\
                           .order_by(sort_option[sort])[offset:offset+limit]

            result = [{
                'thumbnail_image_url': product.thumbnail_image_url,
                'name'               : product.name,
                'price'              : product.price,
                'tags'               : [product_tag.tag.name for product_tag in product.tagproduct_set.all()]
            } for product in products]

            return JsonResponse({'message': result}, status=200)

        except Product.DoesNotExist:
            return JsonResponse({'message': 'product_not_exist'}, status=400)

