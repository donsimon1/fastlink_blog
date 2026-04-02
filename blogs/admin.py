from django.contrib import admin
from .models import Category, BlogPost, Comment


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    # admin table list display
    list_display = ('title', 'category', 'author',
                    'status', 'is_featured', 'created_at')
    list_filter = ('status', 'is_featured', 'category', 'created_at')
    search_fields = ('id', 'title', 'category__category_name',  'status')
    list_editable = ('status', 'is_featured')

class CategoryAmin(admin.ModelAdmin):
    list_display = ('category_name', 'updated_at', 'created_at')


class CommentAmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'updated_at', 'created_at')
# Register your models here.
admin.site.register(Category, CategoryAmin)
admin.site.register(BlogPost, BlogAdmin)
admin.site.register(Comment, CommentAmin)
