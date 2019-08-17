from django.urls import path
from . import views

urlpatterns = [
   path('dashboard/',views.dashboard,name='dashboard'),
    path('add_category/',views.add_category,name='add_category'),
    path('add_subcategory/',views.add_subcategory,name='add_subcategory'),
    path('add_post/',views.add_post,name='add_post'),
    path('all_categories/',views.all_categories,name='all_categories'),
    path('all_posts/',views.all_posts,name='all_posts'),
    path('update_categories/<int:cat_id>',views.update_category,name='update_category'),
    path('delete_categories/<int:cat_id>',views.delete_category,name='delete_category'),
    path('update_posts/<int:post_id>',views.update_post,name='update_post'),
    path('delete_post/<int:post_id>',views.delete_post,name='delete_post'),




]
