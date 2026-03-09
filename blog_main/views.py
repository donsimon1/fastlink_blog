from django.shortcuts import render
from blogs.models import Category
from blogs.models import BlogPost
from assignments.models import About



def home(request):
    featured_posts = BlogPost.objects.filter(
        is_featured=True, status="published").order_by('-updated_at')
    # draft_posts = BlogPost.objects.filter(status='draft')
    posts = BlogPost.objects.filter(is_featured=False, status="Published")
    print(posts)

    # Fetch about us
    try:
        about = About.objects.get()
    except: None
        

    context = {
        "featured_posts": featured_posts,
        #     "draft_posts": draft_posts,
        "posts": posts,
        'about': about
    }
    return render(request, "home.html", context)


