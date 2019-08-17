from django.shortcuts import render,redirect,HttpResponseRedirect
from news.models import Post,Comment,SubCategory,Category
from django.contrib import  messages
from django.contrib.auth.decorators import login_required
from.forms import categoryform,subcategoryform,postform,commentform
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView,UpdateView,DeleteView

# Create your views here.
@login_required()
def dashboard(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    context = {
      'posts':posts,
      'comments':comments,
      'categories':categories,
      'subcategories':subcategories

    }
    return render(request,'dashboard/dashboard.html',context)
@login_required()
def add_category(request):
    if request.method == 'POST':
      cat_form = categoryform(request.POST)
      if cat_form.is_valid():
        cat_form.save()
        messages.success(request,'Category added successfully')
        return redirect('dashboard')
      else:
          messages.warning(request,' the data is not valid')
          return redirect('add_category')

    else:
       cat_form = categoryform()
    context = {'category_form':cat_form}
    return render(request,'dashboard/add_category.html',context)
@login_required()
def add_subcategory(request):
    if request.method == 'POST':
      subcat_form = subcategoryform(request.POST)
      if subcat_form.is_valid():
        subcat_form.save()

        messages.success(request,'SubCategory added successfully')
        return redirect('dashboard')
      else:
          messages.warning(request,' the data is not valid')
          return redirect('add_category')

    else:
       subcat_form = subcategoryform()
    context = {'subcategory_form':subcat_form}
    return render(request,'dashboard/add_subcategory.html',context)
@login_required()
def add_post(request):
    if request.method == 'POST':
      post_form = postform(request.POST,request.FILES)
      if post_form.is_valid():
        post_form.save()

        messages.success(request,'post added successfully')
        return redirect('dashboard')
      else:
          messages.warning(request,' the data is not valid')
          return redirect('add_category')

    else:
       post_form= postform()
    context = {'post_form':post_form}
    return render(request,'dashboard/add_post.html',context)
def all_categories(request):
    context={'cats':Category.objects.all()}
    return render(request,'dashboard/all_categories.html',context)
def all_posts(request):
    context={'posts':Post.objects.all()}
    return render(request,'dashboard/all_posts.html',context)
@login_required()
def update_category(request,cat_id):
    category= Category.objects.get(id=cat_id)
    if request.method == 'POST':
      cat_form = categoryform(request.POST,instance=category)
      if cat_form.is_valid():
        cat_form.save()
        messages.success(request,'Category updated successfully')
        return redirect('/dashboard/all_categories')
      else:
          messages.warning(request,' the data is not valid')


    else:
       cat_form = categoryform(instance=category)
    context = {'updatecategory_form':cat_form}
    return render(request,'dashboard/update_category.html',context)
@login_required()
def delete_category(request,cat_id):
    deleted_cat = Category.objects.get(id=cat_id)
    deleted_cat.delete()
    return redirect('/dashboard/all_categories')
@login_required()
def update_post(request,post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
      post_form = postform(request.POST,request.FILES,instance=post)
      if post_form.is_valid():
        post_form.save()
        messages.success(request,'post updated successfully')
        return redirect('/post_details/'+str(post_id))
      else:
          messages.warning(request,' the data is not valid')


    else:
       post_form = postform(instance=post)
    context = {'updatepost_form':post_form}
    return render(request,'dashboard/update_post.html',context)
@login_required()
def delete_post(request,post_id):
    deleted_post = Post.objects.get(id=post_id)
    deleted_post.delete()
    return redirect('/dashboard/all_posts')
def search(request):
    return redirect('post_details')
