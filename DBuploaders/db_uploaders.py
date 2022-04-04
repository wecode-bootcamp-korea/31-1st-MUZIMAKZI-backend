import os, csv, sys
import django

os.chdir(".")
# print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'MUZIMAKZI.settings')
django.setup()

from products.models import *
from users.models import *
from carts.models import *

# category 외래키 없음.
def insert_category():
    CSV_PATH = './muzimakzi_data/categories.csv'

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
    CSV_PATH = './muzimakzi_data/colors.csv'

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
    CSV_PATH = './muzimakzi_data/images.csv'

    with open(CSV_PATH) as in_file:
        data_reader = csv.reader(in_file)
        for row in data_reader:
            if 'id' in row:
                continue

            image_url  = row[3]
            product_id = row[4]

            Image.objects.create(
                image_url = image_url,
                product_id= product_id
            )

# products 외래키 있음.
def insert_products():
    CSV_PATH = './muzimakzi_data/products.csv'

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
                name                   = name,
                price                  = price,
                description            = description,
                thumbnail_image_url    = thumbnail_image_url,
                type_id                = type_id
            )

# products_options 외래키 있음.
def insert_products_options():
    CSV_PATH = './muzimakzi_data/products_options.csv'

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
                product_id = product_id,
                size_id    = size_id,
                color_id   = color_id,
                stock      = stock
            )

# sizes 외래키 없음.
def insert_sizes():
    CSV_PATH = './muzimakzi_data/sizes.csv'

    with open(CSV_PATH) as in_file:
        data_reader = csv.reader(in_file)
        for row in data_reader:
            if 'id' in row:
                continue

            name = row[1]

            Size.objects.create(name=name)


def insert_tags():
    CSV_PATH = './muzimakzi_data/tags.csv'

    with open(CSV_PATH) as in_file:
        data_reader = csv.reader(in_file)
        for row in data_reader:
            if 'id' in row:
                continue

            tag = row[1]

            Tag.objects.create(tag=tag)

def insert_type():
    CSV_PATH = './muzimakzi_data/types.csv'

    with open(CSV_PATH) as in_file:
        data_reader = csv.reader(in_file)
        for row in data_reader:
            if 'id' in row:
                continue

            type_name = row[1]
            thumbnail_image_url = row[2]
            category_id = row[3]

            Type.objects.create(
                name                = type_name,
                thumbnail_image_url = thumbnail_image_url,
                category_id         = category_id
            )

def insert_cart():
    CSV_PATH = './muzimakzi_data/carts.csv'

    with open(CSV_PATH) as in_file:
        data_reader = csv.reader(in_file)
        for row in data_reader:
            if 'id' in row:
                continue

            quantity = row[3]
            product_option_id = row[4]
            user_id = row[5]

            Cart.objects.create(
                user_id = user_id,
                product_option_id = product_option_id,
                quantity = quantity
            )

def insert_user():
    CSV_PATH = './muzimakzi_data/users.csv'

    with open(CSV_PATH) as in_file:
        data_reader = csv.reader(in_file)
        for row in data_reader:
            if 'id' in row:
                continue

            first_name = row[3]
            last_name = row[4]
            email = row[5]
            password = row[6]
            phone_number = row[7]

            User.objects.create(
                first_name= first_name,
                last_name = last_name,
                email = email,
                password= password,
                phone_number=phone_number
            )


insert_user()
insert_category()
insert_type()
insert_products()
insert_images()
insert_tags()
insert_sizes()
insert_color()
insert_products_options()
insert_cart()
