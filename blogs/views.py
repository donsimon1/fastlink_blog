from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import BlogPost
from .models import Category

# Create your views here.


def post_by_category(request, pk):
    # fetch the posts that belongs to the category with id=pk
    posts = BlogPost.objects.filter(category_id=pk, status='published')
    category = get_object_or_404(Category, id=pk)
    # categories data can be added here if needed in the template
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'category': category,
        'categories': categories,
    }
    return render(request, 'post_by_category.html', context)
 