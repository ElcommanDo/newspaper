from django.shortcuts import render,redirect
from .forms import Admin_form
from .models import Category,Post,Comment
from dashboard.forms import commentform
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def home(request):
    posts = Post.objects.all()

    context = {'posts':posts}
    return render(request,'news/index.html',context)
def post_details(request,post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
      comment_form = commentform(request.POST)
      if comment_form.is_valid():
        post = Post.objects.get(id = post_id)
        new_comment=comment_form.save(commit=False)
        new_comment.post = post
        new_comment.save()
        comment_form= commentform()
    else:
      comment_form= commentform()
    context={'post':post,'comment_form':comment_form,'comments':comments}
    return render(request,'news/post_details.html',context)
def category_details(request,cat_id):
    cat = Category.objects.get(id=cat_id)
    posts = Post.objects.filter(category=cat)

    context = {'category':cat,'posts':posts}
    return render(request,'news/category_details.html',context)
def login_Admin(request):

    if request.method == 'POST':
        adminForm = Admin_form(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        admin = authenticate(request,username=username,password=password)
        if admin is not None:
          login(request,admin)
          messages.success(request, '{} logged in successfully'.format(username))
          return redirect('/dashboard/dashboard')
        else:
            messages.warning(request,'this username  is not authorized to login ')
            return redirect('login')
    else:
        adminForm = Admin_form()
    return render(request,'news/login.html',{'form':adminForm})
@login_required()
def logout_user(request):
    logout(request)
    messages.success(request,'{} logged out successfully '.format(request.user.username))
    return redirect('home')
