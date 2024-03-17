from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField

role_options = {
    'vocals': 'Vocals',
    'guitars':'Guitars',
    'bass': 'Bass',
    'keyboards': 'Keyboards',
    'tin whistle': 'Tin Whistle',
    'lyre': 'Lyre',
    'mix': 'Mix',
    'master': 'Master'
}

def generate_slug(value):
    return slugify(value.replace(' ', '-'))

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=500)
    country = models.TextField()
    member_image = models.ImageField(null=True)
    description = models.TextField()
    role = models.CharField(max_length=12,choices=role_options, default='vocals')
    equipament = models.TextField()

    def __str__(self):
        return self.name

class About(models.Model):
    description = models.TextField()
    emblem = models.ImageField(null=True)
    label = models.CharField(max_length=1000, blank=True)
    label_email = models.EmailField(default='kublaikapsalis@gmail.com')
    label_number = models.CharField(max_length=17, blank=True)
    management = models.CharField(max_length=2000, blank=True)
    testimonial = models.TextField(null=True)
    testimonial_by = models.TextField(null=True)
    testimonial_from = models.TextField(null=True, blank=True)
    management_email = models.EmailField(default='elenionofficial@gmail.com')
    management_number = models.CharField(max_length=17, blank=True) # Validators should be a list
    press_request = models.CharField(max_length=2000, blank=True)
    press_email = models.EmailField(default='elenionofficial@gmail.com')
    press_number = models.CharField(max_length=17, blank=True)
    booking = models.CharField(max_length=2000, blank=True)
    booking_email = models.EmailField(default='elenionofficial@gmail.com')
    booking_number = models.CharField(max_length=17, blank=True)

class New(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.TextField(null=True, blank=True)
    first_description = models.TextField(null=True, blank=True)
    second_description = models.TextField(null=True, blank=True)
    testimonial = models.TextField(null=True, blank=True)
    testimonial_by = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(null=True)
    created_at = models.DateField(auto_now_add=True)
    original_released_date = models.DateField(null=True)
    original_post = models.URLField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    slug = AutoSlugField(populate_from='title', slugify=generate_slug)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.TextField()
    cover = models.ImageField(null=True)
    released_at = models.DateField()
    tracklist = models.ManyToManyField('Music', related_name='musics', blank=True)

    def __str__(self):
        return self.title

class Music(models.Model):
    title = models.TextField()
    thumbnail = models.ImageField(null=True)
    author = models.ForeignKey(Member, on_delete=models.PROTECT)
    album = models.ForeignKey(Album, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
