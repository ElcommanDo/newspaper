from django import template
from news.models import Category,Post
register = template.Library()
@register.inclusion_tag('news/categories.html')

def all_categories():
    categs = Category.objects.all()
    context = {'categories':categs}
    return context
@register.inclusion_tag('news/recentNews.html')
def recent_news():
    context = {
        'posts':Post.objects.all()[0:6],
    }
    return context
