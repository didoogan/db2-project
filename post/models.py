from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    title = models.CharField(max_length=50)
    content = models.TextField()
    published = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.author.email, self.title)
