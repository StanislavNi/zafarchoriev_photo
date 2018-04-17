from django.db import models
from django.utils import timezone

SECTIONS = (
    ('portrait', 'portrait'),
    ('city', 'city'),
    ('daily', 'daily'),
)

class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    photo = models.ImageField(upload_to='images', blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    section = models.CharField(max_length=200, null=True, choices=SECTIONS)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
