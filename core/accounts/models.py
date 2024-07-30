from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils.translation import ugettext_lazy as _

class Usermanager(BaseUserManagers):
    
    def create_user(self,email,passwoed,**extra_fields):
        if not email:
            raise ValueError(_("the email must be set."))
        email=self.normalize_emil(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(passwoed)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Super user must have is_staff=True !"))
        if extra_fields.get('is_superuser') is not True :
            raise ValueError(_("Super user must hava is_superuser=True !"))
        
        return self.create_user(email,password,**extra_fields)
    
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD='email'
    
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    
    def __str__ (self):
        return self.email