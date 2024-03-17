# Generated by Django 5.0.2 on 2024-03-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='product_images')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=300)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('color', models.CharField(choices=[('black', 'Black'), ('white', 'White'), ('grey', 'Grey')], max_length=10)),
                ('size', models.CharField(choices=[('xx-small', 'XXS'), ('x-small', 'XS'), ('small', 'S'), ('medium', 'M'), ('large', 'L'), ('x-large', 'XL'), ('xx-large', 'XXL')], max_length=10)),
                ('material', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('original_release', models.DateField()),
                ('posted_at', models.DateField(auto_now_add=True)),
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_format', models.CharField(choices=[('lp', 'LP'), ('vinyl', 'Vinyl')], max_length=100)),
                ('in_stock', models.CharField(choices=[('in stock', 'In Stock'), ('sold out', 'Sold Out')], max_length=10)),
                ('images', models.ManyToManyField(blank=True, related_name='products', to='shop.productimage')),
            ],
        ),
    ]