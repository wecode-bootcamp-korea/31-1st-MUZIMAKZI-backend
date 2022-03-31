import os, csv
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'MUZIMAKZI.settings')
django.setup()

from products.models import *
from users.models import *
from carts.models import *

# category 외래키 없음.
def insert_category():
    CSV_PATH = './DBuploaders/muzimakzi_data/categories.csv'

    with open(CSV_PATH) as in_file:
        data_reader = csv.reader(in_file)
        for row in data_reader:
            if 'id' in row:
                continue

            category_name = row[1]

            Category.objects.create(
                name = category_name
            )

# color 외래키 없음.
def insert_color():
    CSV_PATH = './DBuploaders/muzimakzi_data/colors.csv'

    with open(CSV_PATH) as in_file:
        data_reader = csv.reader(in_file)
        for row in data_reader:
            if 'id' in row:
                continue

            name = row[1]

            Color.objects.create(
                name=name
            )

# images 외래키 있음.
def insert_images():
    CSV_PATH = './DBuploaders/muzimakzi_data/images.csv'

    with open(CSV_PATH) as in_file:
        data_reader = csv.reader(in_file)
        for row in data_reader:
            if 'id' in row:
                continue

            image_url  = row[3]
            product_id = row[4]

            Product.objects.create(
                image_url = image_url,
                product= Product.objects.get(id=product_id).id
            )

# products 외래키 있음.
def insert_products():
    CSV_PATH = './DBuploaders/muzimakzi_data/products.csv'

    with open(CSV_PATH) as in_file:
        data_reader = csv.reader(in_file)
        for row in data_reader:
            if 'id' in row:
                continue

            name = row[3]
            price = row[4]
            description = row[5]
            thumbnail_image_url = row[6]
            type_id = row[7]

            Product.objects.create(
                name                = name,
                price               = price,
                description         = description,
                thumbnail_image_url = thumbnail_image_url,
                type                = Type.objects.get(id=type_id).id
            )

# products_options 외래키 있음.
def insert_products_options():
    CSV_PATH = './DBuploaders/muzimakzi_data/products_options.csv'

    with open(CSV_PATH) as in_file:
        data_reader = csv.reader(in_file)
        for row in data_reader:
            if 'id' in row:
                continue

            stock       = row[1]
            color_id    = row[2]
            product_id  = row[3]
            size_id     = row[4]

            ProductOption.objects.create(
                product = Product.objects.get(id=product_id).id,
                size    = Size.objects.get(id=size_id).id,
                color   = Color.objects.get(id=color_id).id,
                stock   = stock
            )

# sizes 외래키 없음.
def insert_sizes():
    CSV_PATH = './DBuploaders/muzimakzi_data/sizes.csv'

    with open(CSV_PATH) as in_file:
        data_reader = csv.reader(in_file)
        for row in data_reader:
            if 'id' in row:
                continue

            name = row[1]

            Size.objects.create(name=name)


def insert_tags():
    CSV_PATH = './DBuploaders/muzimakzi_data/tags.csv'

    with open(CSV_PATH) as in_file:
        data_reader = csv.reader(in_file)
        for row in data_reader:
            if 'id' in row:
                continue

            tag = row[1]

            Tag.objects.create(tag=tag)

def insert_type():
    CSV_PATH = './DBuploaders/muzimakzi_data/types.csv'

    with open(CSV_PATH) as in_file:
        data_reader = csv.reader(in_file)
        for row in data_reader:
            if 'id' in row:
                continue

            type_name = row[1]
            thumbnail_image_url = row[2]
            category_id = row[3]

            Type.objects.create(
                name=type_name,
                thumbnail_image_url= thumbnail_image_url,
                category_id= category_id
            )

def insert_cart():
    CSV_PATH = './DBuploaders/muzimakzi_data/carts.csv'

    with open(CSV_PATH) as in_file:
        data_reader = csv.reader(in_file)
        for row in data_reader:
            if 'id' in row:
                continue

            user_id = row[5]
            quantity = row[3]
            product_option_id = row[4]


            Cart.objects.create(
                user = User.objects.get(id=user_id).id,
                product_option = ProductOption.objects.get(id=product_option_id).id,
                quantity = quantity
            )

def insert_user():
    CSV_PATH = './DBuploaders/muzimakzi_data/users.csv'
    pass
    #
    # with open(CSV_PATH) as in_file:
    #     data_reader = csv.reader(in_file)
    #     for row in data_reader:
    #         if 'id' in row:
    #             continue
    #
    #         User.objects.create(
    #             user
    #         product_option
    #         quantity
    #         )






# os.chdir('.')
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'MUZIMAKZI.settings')
# django.setup()
#
# CSV_PATH     = './DBuploaders/muzimakzi_data'
# file_list    = os.listdir(CSV_PATH)
#
# # table_name = []
# # for file in file_list:
# #     table_name.append(file.split('.csv'))
#
#
# for file in file_list:
#     with open(file, newline='', encoding='utf8') as csvfile:
#         rows = csv.reader(csvfile, delimiter=',')
