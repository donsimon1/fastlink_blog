from django import forms
from .models import Category, BlogPost


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['category_name']

        widgets = {
            'category_name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-3 py-2 focus:ring-2 focus:ring-green-500',
                'placeholder': 'Enter category name'
            }),
        }


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = [
            'title',
            'category',
            'featured_image',
            'short_description',
            'blog_body',
            'status',
            'is_featured'
        ]

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-3 py-2',
                'placeholder': 'Enter blog title'
            }),

            'category': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-3 py-2'
            }),

            'featured_image': forms.ClearableFileInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-3 py-2'
            }),

            'short_description': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-3 py-2',
                'placeholder': 'Short description of the blog'
            }),

            'blog_body': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-3 py-2',
                'rows': 6,
                'placeholder': 'Write your blog content here'
            }),

            'status': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-3 py-2'
            }),

            'is_featured': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-green-600 border-gray-300 rounded'
            }),
        }
