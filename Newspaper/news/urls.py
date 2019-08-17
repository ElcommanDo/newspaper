from django.urls import path
from .views import home,post_details, category_details
urlpatterns = [
    path('',home,name='home'),
    path('post_details/<int:post_id>',post_details,name='post_details'),
    path('category_details/<int:cat_id>',category_details,name='category_details'),

]
