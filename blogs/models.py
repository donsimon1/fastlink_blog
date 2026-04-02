from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="posts")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="authors")
    featured_image = models.ImageField(
        upload_to='uploads/%Y/%m/%d/', blank=True, null=True)
    short_description = models.CharField(max_length=500)
    blog_body = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES,
                              default='draft', max_length=10)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
