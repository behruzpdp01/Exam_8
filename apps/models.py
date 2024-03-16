from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, ImageField, BigIntegerField, ForeignKey, CASCADE


class User(AbstractUser):
    username = CharField(unique=True, max_length=255)
    email = CharField(unique=True, max_length=255)
    password = CharField(max_length=255)


class Category(Model):
    name = CharField(max_length=255)


class Product(Model):
    user = ForeignKey('apps.User', CASCADE)
    name = CharField(max_length=255)
    text = CharField(max_length=255)
    color = CharField(max_length=255)
    price = BigIntegerField()
    description = CharField(max_length=255)
    category = ForeignKey('apps.Category', CASCADE)

    def __str__(self):
        return self.name


class ProductImage(Model):
    product = ForeignKey('apps.Product', CASCADE)
    image = ImageField(upload_to='image', default='default.jpg')
