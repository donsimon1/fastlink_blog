import sweetify
from django.shortcuts import redirect, render
from blogs.models import Category
from blogs.models import BlogPost
from assignments.models import About
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def home(request):
    featured_posts = BlogPost.objects.filter(
        is_featured=True, status="published").order_by('-updated_at')
    # draft_posts = BlogPost.objects.filter(status='draft')
    posts = BlogPost.objects.filter(is_featured=False, status="Published")
    print(posts)

    # Fetch about us
    try:
        about = About.objects.get()
    except:
        None

    context = {
        "featured_posts": featured_posts,
        #     "draft_posts": draft_posts,
        "posts": posts,
        'about': about
    }
    return render(request, "home.html", context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {"form": form}
    return render(request, 'register.html', context)


def login(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()  # ✅ cleaner than manual authenticate

            auth.login(request, user)

            # ✅ Success SweetAlert (modal style)
            sweetify.toast(
                request,
                "You are logged in successfully",
                icon="success",
                position="top-end",   # 👈 top-right
                timer=2500,           # disappears quickly
                width="400px",        # small size
                showConfirmButton=False
            )

            return redirect('dashboard')

        else:
            # ❌ Error SweetAlert
            sweetify.toast(
                request,
                "Invalid username or password",
                icon="error",
                position="top-end",   # 👈 top-right
                timer=2500,           # disappears quickly
                width="400px",        # small size
                showConfirmButton=False
            )

            return redirect('login')  # important for messages to show

    return render(request, 'login.html', {'form': form})


def logout(request):
    auth.logout(request)

    # ✅ Small top-right toast
    sweetify.toast(
        request,
        "You have been logged out 👋",
        icon="success",
        position="top-end",
        timer=2500,
        showConfirmButton=False
    )
    return redirect('login')
