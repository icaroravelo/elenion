# Generated by Django 5.0.2 on 2024-03-16 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('video_by', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('mix', models.TextField(blank=True, null=True)),
                ('master', models.TextField(blank=True, null=True)),
                ('video_url', models.URLField()),
                ('released_at', models.DateField()),
            ],
        ),
    ]
