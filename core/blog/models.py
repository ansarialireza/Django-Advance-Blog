from django.db import models
from django.contrib.auth import get_user_model

# getting user model object
# User = get_user_model()

class Post(models.Model):
    '''
    this is a class to define posts for blog app
    
    '''
    author = models.ForeignKey('accounts.Profile',on_delete=models.CASCADE)
    image = models.ImageField()
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    published_date = models.DateField()
    
    def __str__ (self):
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__ (self):
        return self.name