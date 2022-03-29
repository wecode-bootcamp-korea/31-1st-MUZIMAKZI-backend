from django.db import models


class Cart(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.Model)
    product_option_id = models.ForeignKey('products.products_options', on_delete=models.Model, related_name='carts')
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'carts'