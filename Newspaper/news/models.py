from django.db import models
from django.contrib.auth.models import User
from passlib.hash import pbkdf2_sha256

# Create your models here.
'''
class Admin(models.Model):
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=20)
    def password_ecrypt(self,):
        self.password = pbkdf2_sha256.encrypt(self.password,rounds=12000,salt_size=32)
        return self.password

    def __str__(self):
        return self.username
        '''
class Category(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    def __str__(self):
        return self.title
class SubCategory(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category =models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    post_date = models.DateTimeField(null=True, blank=True ,auto_now_add=True)
    image = models.ImageField(blank=True,null=True,upload_to='post_pics')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ('-post_date',)
class Comment(models.Model):
    title = models.CharField(blank=True ,null= True,max_length=50)
    content = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    post_date = models.DateTimeField(null=True, blank=True ,auto_now_add=True)
    def __str__(self):
        return self.content

