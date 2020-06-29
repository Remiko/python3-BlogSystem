from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField


# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length=10)

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    title = models.CharField(max_length=30)
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE)
    content = MDTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']
