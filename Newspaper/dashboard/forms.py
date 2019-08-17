from django import forms
from news.models import Category,Post,Comment,SubCategory
class commentform(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('title','content')
class postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','category','subcategory','admin','image')
class categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title','content')
class subcategoryform(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ('title','content','category')
