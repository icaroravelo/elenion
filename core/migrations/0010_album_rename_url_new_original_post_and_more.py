# Generated by Django 5.0.2 on 2024-03-16 12:31

import autoslug.fields
import core.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_about_booking_number_about_label_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('cover', models.ImageField(null=True, upload_to='')),
                ('released_at', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='new',
            old_name='url',
            new_name='original_post',
        ),
        migrations.AddField(
            model_name='new',
            name='original_released_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='new',
            name='subtitle',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='new',
            name='testimonial',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='new',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', slugify=core.models.generate_slug),
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('thumbnail', models.ImageField(null=True, upload_to='')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.album')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.member')),
            ],
        ),
    ]