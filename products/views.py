from django.db.models   import Q
from products.models    import Type, Product

from django.http        import JsonResponse
from django.views       import View


class TypeView(View):
    def get(self, request, category_id):
        try:
            types = Type.objects.filter(category=category_id)

            results = [{
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

            products = Product.objects.filter(condition).order_by(sort)[offset:offset+limit]

            results = [{
                'product_id'         : product.id,
                'thumbnail_image_url': product.thumbnail_image_url,
                'name'               : product.name,
                'price'              : product.price,
                'tags'               : [tags.tag.name for tags in product.tagproduct_set.all()]
            } for product in products if len(product.tagproduct_set.all()) >= len(tags)]

            return JsonResponse({'message': results}, status=200)

        except Product.DoesNotExist:
            return JsonResponse({'message': 'product_not_exist'}, status=400)

