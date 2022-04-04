from django.db import models

from core.models import TimeStampedModel


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categories'

class Type(models.Model):
    name                = models.CharField(max_length=100)
    thumbnail_image_url = models.URLField(max_length=2000)
    category            = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'types'

class Product(TimeStampedModel):
    name                  = models.CharField(max_length=500)
    price                 = models.DecimalField(max_digits=9, decimal_places=2)
    description           = models.TextField()
    thumbnail_image_url   = models.URLField(max_length=2000)
    type                  = models.ForeignKey('Type', on_delete=models.CASCADE)
    tag                   = models.ManyToManyField('Tag',through='TagProduct')

    class Meta:
        db_table = 'products'

class Tag(models.Model):
    name     = models.CharField(max_length=100)

    class Meta:
        db_table = 'tags'

class TagProduct(models.Model):
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tags_products'

class ProductOption(models.Model):
    product  = models.ForeignKey('Product', on_delete=models.CASCADE)
    size     = models.ForeignKey('Size', on_delete=models.CASCADE)
    color    = models.ForeignKey('Color', on_delete=models.CASCADE)
    stock    = models.IntegerField(default=1)

    class Meta:
        db_table = 'products_options'

class Image(TimeStampedModel):
    image_url = models.URLField(max_length=2000)
    product   = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Size(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'sizes'

class Color(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'colors'


class Promote(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField(max_length=2000)

    class Meta:
        db_table = 'promotes'

class Landing(models.Model):
    image_url = models.URLField(max_length=2000)

    class Meta:
        db_table = 'landing_images'