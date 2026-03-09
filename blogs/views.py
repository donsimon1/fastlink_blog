from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import BlogPost
from .models import Category
from django.db.models import Q
from blogs.forms import BlogPostForm

# Create your views here.


def post_by_category(request, pk):
    # fetch the posts that belongs to the category with id=pk
    posts = BlogPost.objects.filter(
        category_id=pk, status='published')
    # Use try/except when we want to perform some action
    try:
        category = get_object_or_404(Category, id=pk)
    except:
        # redirect the user to the home page
        return redirect("home")
    # Use get_object_or_404 when you want to show 404 error page if the category does not exist
    # category = get_object_or_404(Category, id=pk)
    # categories data can be added here if needed in the template

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_by_category.html', context)


def blogs(request, slug):
    single_blog = get_object_or_404(BlogPost, slug=slug, status="published")
    context = {"single_blog": single_blog}
    return render(request, 'blogs.html', context)


def search(request):
    keyword = request.GET["keyword"]
    blogs = BlogPost.objects.filter(Q(title__icontains=keyword) | Q(
        short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status="Published")
    context = {"blogs": blogs, "keyword": keyword}
    return render(request, 'search.html', context)


def create_post(request):
    form = BlogPostForm()

    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

    return render(request, "blogs/create_post.html", {"form": form})
