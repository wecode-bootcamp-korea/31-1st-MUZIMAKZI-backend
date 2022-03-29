from django.db import models

from users.models import TimeStampedModel


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name


class Type(models.Model):
    name      = models.CharField(max_length=100)
    thumbnail = models.URLField(max_length=2000)
    category  = models.ForeignKey('Category', related_name='category_type', on_delete=models.CASCADE)

    class Meta:
        db_table = 'types'

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    name        = models.CharField(max_length=500)
    price       = models.DecimalField(max_digits=9, decimal_places=3)
    description = models.TextField()
    thumbnail   = models.URLField(max_length=2000)
    tag         = models.CharField(max_length=100)
    type        = models.ForeignKey('Type', related_name='product_type', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name


class Product_option(models.Model):
    product = models.ForeignKey('Product', related_name='option_product', on_delete=models.CASCADE)
    size    = models.ForeignKey('Size', related_name='product_size', on_delete=models.CASCADE)
    color   = models.ForeignKey('Color', related_name='product_color', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_options'

    def __str__(self):
        return self.product


class Image(TimeStampedModel):
    image_url = models.URLField(max_length=2000)
    product   = models.ForeignKey('Product', related_name='product_image', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

    def __str__(self):
        return self.product


class Size(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'sizes'

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'colors'

    def __str__(self):
        return self.name