from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import BlogPost
from .models import Category, Comment
from django.db.models import Q


# Create your views here.


def post_by_category(request, pk):
    # fetch the posts that belongs to the category with id=pk
    posts = BlogPost.objects.filter(
        category_id=pk, status='published')
    # try:
    #     category = get_object_or_404(Category, pk=pk)
    # except:
    #     return redirect('home')
    category = get_object_or_404(Category, pk=pk)

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_by_category.html', context)


def blogs(request, slug):
    single_blog = get_object_or_404(BlogPost, slug=slug, status="published")
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    context = {
        "single_blog": single_blog,
        'comments': comments,
        'comment_count': comment_count,
    }
    return render(request, 'blogs.html', context)


def search(request):
    keyword = request.GET["keyword"]
    blogs = BlogPost.objects.filter(Q(title__icontains=keyword) | Q(
        short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status="Published")
    context = {"blogs": blogs, "keyword": keyword}
    return render(request, 'search.html', context)


def landing_page(request):
    return render(request, 'landing_page.html')
