from django.utils import timezone
from django.db import models
# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.username
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
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ('-post_date',)
class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    post_date = models.DateTimeField(null=True, blank=True ,auto_now_add=True)
    def __str__(self):
        return self.content

