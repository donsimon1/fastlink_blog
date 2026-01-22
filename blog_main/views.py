from django.shortcuts import render
from blogs.models import Category
from blogs.models import BlogPost


def home(request):
    # categories = Category.objects.all()
    # featured_posts = BlogPost.objects.filter(is_featured=True, status ="published").order_by('-updated_at')
    # draft_posts = BlogPost.objects.filter(status='draft')
    # posts = BlogPost.objects.filter(status='published')
    
    # context = {
    #     "categories": categories,
    #     "featured_posts": featured_posts,
    #     "draft_posts": draft_posts,
    #     "posts": posts,
    # }
    return render(request, "home.html")
