from django.shortcuts import render
#from .models import Category,Post,Comment,SubCategory,Admin
# Create your views here.
def home(request):
    return render(request,'news/index.html')
