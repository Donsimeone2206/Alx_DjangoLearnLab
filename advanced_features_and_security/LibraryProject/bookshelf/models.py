from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager
from django.apps import AppConfig
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} year {int(self.publication_year)}"
    
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True , blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/')

   
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["date_of_birth" ,"profile_photo"]

    def __str__(self):
        return self.username
    object = 'CustomUserManager'

    

class CustomUserManager(BaseUserManager):
    def create_user(self,username,  date_of_birth , profile_photo, password=None):
        if not username:
            raise ValueError("The Username field must be set")
        if not date_of_birth:
            raise ValueError("User must enter date of birth")
        if not profile_photo:
            raise ValueError("User must place profile photo")
        user = self.model(
        username = username,
        date_of_birth = date_of_birth,
        profile_photo = profile_photo
    )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username, date_of_birth, profile_photo, password =None):
        user = self.create_user( username,date_of_birth, profile_photo, password =password)
        
        user.is_staff =True

        user.is_superuser = True
        user.save(using= self._db)
        return user

class Model(models.Model):
    class Meta:[ # creating the meta class
        ("can_view", "can view"), # creating permisions
        ("can_create", "can create"), # creating permissions
        ("can_edit", "can edit"), # creating permissions
        ("can_delete", "can delete "), # creating permissions
    ]
from django.contrib.auth.models import Group , Permission
from django.contrib.auth.models import User
class BookshelfConfig(AppConfig):
    name = 'bookshelf'
    def ready(self):
        
        from django.contrib.auth.models import Group , Permission
        from django.contrib.auth.models import User
        
        editors_group , created = Group.objects.get_or_create(name = "Editors") # creating groups
        viewers_group , created = Group.objects.get_or_create(name = "Viewers")# creating groups
        admins_group , created = Group.objects.get_or_create(name = "Admins") # creating groups


        edit_permission = Permission.objects.get(codename = 'can_edit')
        create_permission = Permission.objects.get(codename = 'can_create')

        editors_group.permissions.add([edit_permission , create_permission]) # assigning appropriate permissions to each group.

        user = User.objects.get(username='xteve') # creating test users
         
        editors_group.user_set.add('xteve')# assigning a user to a group
