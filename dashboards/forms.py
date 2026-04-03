from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from blogs.models import BlogPost, Category


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            "title",
            "category",
            "featured_image",
            "short_description",
            "blog_body",
            "status",
            "is_featured",
        ]
        """
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Enter blog title"
            }),
            "category": forms.Select(attrs={
                "class": "w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            }),
            "featured_image": forms.FileInput(attrs={
                "class": "w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            }),
            "short_description": forms.Textarea(attrs={
                "class": "w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500",
                "rows": 3,
                "placeholder": "Brief summary of the post"
            }),
            "blog_body": forms.Textarea(attrs={
                "class": "w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500",
                "rows": 6,
                "placeholder": "Write your blog content here..."
            }),
            "status": forms.Select(attrs={
                "class": "w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            }),
            "is_featured": forms.CheckboxInput(attrs={
                "class": "h-4 w-4 text-blue-600 border-gray-300 rounded"
            }),
        }
"""

class CategorytForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active',
                  'is_staff', 'is_superuser', 'groups', 'user_permissions')


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active',
                  'is_staff', 'is_superuser', 'groups', 'user_permissions')

        # widgets = {
        #     "username": forms.TextInput(attrs={
        #         "class": "w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500",
        #         "placeholder": "Enter blog title"
        #     }),
        #     "email": forms.EmailInput(attrs={
        #         "class": "w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        #     }),
        #     "first_name": forms.TextInput(attrs={
        #         "class": "w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        #     }),
        #     "last_name": forms.TextInput(attrs={
        #         "class": "w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500",
        #         "placeholder": "Brief summary of the post"
        #     }),
        #     "is_active": forms.CheckboxInput(attrs={
        #         "class": "h-4 w-4 text-blue-600 border-gray-300 rounded"
        #     }),
        #     "is_staff": forms.CheckboxInput(attrs={
        #         "class": "h-4 w-4 text-blue-600 border-gray-300 rounded"
        #     }),
        #     "is_superuser": forms.CheckboxInput(attrs={
        #         "class": "h-4 w-4 text-blue-600 border-gray-300 rounded"
        #     }),
        #     "groups": forms.Select(attrs={
        #         "class": "h-4 w-4 text-blue-600 border-gray-300 rounded"
        #     }),
        # }
