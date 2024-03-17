from django.db import models

# Color options
COLOR_OPTIONS = [
    ('black', 'Black'),
    ('white', 'White'),
    ('grey', 'Grey'),
]

# Size options
SIZE_OPTIONS = [
    ('xx-small', 'XXS'),
    ('x-small', 'XS'),
    ('small', 'S'),
    ('medium', 'M'),
    ('large', 'L'),
    ('x-large', 'XL'),
    ('xx-large', 'XXL'),
]

# Product format options 
FORMAT_OPTIONS = [
    ('lp', 'LP'),
    ('vinyl', 'Vinyl'),
    ('poster', 'Poster')
]

STOCK_OPTIONS = [
    ('in stock', 'In Stock'),
    ('sold out', 'Sold Out')
]

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=300)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    color = models.CharField(max_length=10, choices=COLOR_OPTIONS, null=True, blank=True)
    size = models.CharField(max_length=10, choices=SIZE_OPTIONS, null=True, blank=True)
    material = models.TextField(default='', null=True, blank=True)
    prodapp = models.TextField(default='', null=True, blank=True)
    original_release = models.DateField()
    posted_at = models.DateField(auto_now_add=True)
    product_id = models.AutoField(primary_key=True)
    product_format = models.CharField(max_length=100, choices=FORMAT_OPTIONS, null=True, blank=True)
    in_stock = models.CharField(max_length=10, choices=STOCK_OPTIONS, null=True, blank=True)
    images = models.ManyToManyField('ProductImage', related_name='products', blank=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.title