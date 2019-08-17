from django.contrib import admin
from .models import Category,SubCategory,Post,Comment
# Register your models here.

class category(admin.ModelAdmin):
    list_display = ('title','content')
    list_editable = ('content',)
    list_display_links = ('title',)
admin.site.register(Category,category)
class subcategory(admin.ModelAdmin):
    list_display = ('title','content')
    list_editable = ('content',)
    list_display_links = ('title',)

admin.site.register(SubCategory,subcategory)
admin.site.register(Comment)
admin.site.register(Post)

