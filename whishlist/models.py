from django.db import models

from core.models import TimeStampedModel


class WishList(TimeStampedModel):
    user           = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product_option = models.ForeignKey('products.ProductOption', on_delete=models.CASCADE)

    class Meta:
        db_table = 'wish_lists'