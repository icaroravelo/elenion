# Generated by Django 5.0.2 on 2024-03-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_album_rename_url_new_original_post_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='testimonial_by',
            field=models.TextField(blank=True, null=True),
        ),
    ]