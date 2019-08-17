from django import forms
from .models import Post,Category,User,SubCategory,Comment
class Admin_form(forms.ModelForm):
    username = forms.CharField(required=True,max_length=120)
    password = forms.CharField(required=True,max_length=20,widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','password')

