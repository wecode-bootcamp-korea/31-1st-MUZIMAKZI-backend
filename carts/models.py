from django.db import models

from core.models import TimeStampedModel


class Cart(TimeStampedModel):
    user = models.OneToOneField('users.User', on_delete=models.Model)
    product_option_id = models.ForeignKey('products.Product_option', on_delete=models.Model, related_name='carts')
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'carts'