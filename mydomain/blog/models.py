from django.db import models

# Create your models here.

# blog category


# blog tags


# blog post content
class Blog(models.Model):
    """
    blog content
    """
    title = models.CharField('title', max_length=100)
    author = models.CharField('author', max_length=16)
    content = models.TextField('content')
    created = models.DateTimeField('create_time', auto_now_add=True)
    category = models.CharField('category', max_length=50, blank=True)
    tags = models.CharField('tag', max_length=100, blank=True)

    def __str__(self):
        return self.title

# blog comment
class Comment(models.Model):
    """
    comment
    """
    blog = models.ForeignKey(Blog, verbose_name='blog')
    name = models.CharField('username', max_length=16)
    email = models.EmailField('email')
    content = models.TextField('content')
    created = models.DateTimeField('update_time', auto_now_add=True)

    def __str__(self):
        return self.content
