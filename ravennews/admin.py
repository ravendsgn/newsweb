from django.contrib import admin
from .models import Category, News

admin.site.register(Category)
admin.site.register(News)

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'news', 'created_at')
#     search_fields = ('name', 'text', 'news__title')
#     list_filter = ('created_at',)

# admin.site.register(News)