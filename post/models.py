from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    title = models.CharField(max_length=50)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    @property
    def likes_num(self):
        return len(self.likes.all())

    def __str__(self):
        return '{0} "{1}"'.format(self.author.email, self.title)


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='comments')
    post = models.ForeignKey(Post, related_name='comments')
    text = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        text = self.text
        if len(text) > 20:
            text = self.text[20:]
        return '{0} "{1}..."'.format(self.author.email, text)
