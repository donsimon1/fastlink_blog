from django.contrib import admin
from .models import Category
from .models import BlogPost


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    # admin table list display
    list_display = ('title', 'category', 'author',
                    'status', 'is_featured', 'created_at')
    list_filter = ('status', 'is_featured', 'category', 'created_at')
    search_fields = ('id', 'title', 'category__category_name',  'status')
    list_editable = ('status', 'is_featured')


# Register your models here.
admin.site.register(Category)
admin.site.register(BlogPost, BlogAdmin)
