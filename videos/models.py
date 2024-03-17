from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=1000)
    thumbnail = models.ImageField(null=True, blank=True)
    video_by = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mix = models.TextField(blank=True, null=True)
    master = models.TextField(blank=True, null=True)
    video_url = models.URLField()
    released_at = models.DateField()

    def __str__(self):
        return self.title