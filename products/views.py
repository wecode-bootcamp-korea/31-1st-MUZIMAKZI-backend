from django.db.models import Q
from products.models import Type, Product, Tag

from django.http import JsonResponse
from django.views import View


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
            type_id         = int(request.GET.get('type_id'))
            tags            = request.GET.getlist('tags', None)
            sort            = request.GET.get('sort', 'id')
            searching       = request.GET.get('name')
            limit           = int(request.GET.get('limit', 10))
            offset          = int(request.GET.get('offset', 0))

            sort_option = {
                'id'  : 'id',
                'asc': 'price',
                'desc': '-price'
            }

            condition_product = Q()
            condition_tag = Q()

            if type_id:
                condition_product &= Q(type_id=type_id)
            if searching:
                condition_product &= Q(name__icontains=searching)
            if tags:
                condition_tag &= Q(tag__in=tags)

            # 이거 되는거
            # products = Tag.objects.get(tag=tag).products.select_related('type').filter(product_condition)

            tags = Tag.objects.filter(condition_tag)
            print(tags[0].products.filter(condition_product))
            print(tags[1].products.filter(condition_product))

            # result = [{
            #     'name'               : product.name,
            #     'price'              : product.price,
            #     'tags'               : [tag.tag for tag in product.tags.all()],
            #     'thumbnail_image_url': product.thumbnail_image_url
            # } for product in Tag.products.filter(condition_product)]

            # return JsonResponse({'message': result}, status=200)
            return JsonResponse({'message': '도전'}, status=200)

        except Product.DoesNotExist:
            return JsonResponse({'message': 'product_not_exist'}, status=400)

