from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.contrib.auth.password_validation import validate_password

class City(models.Model):
    city = models.CharField(max_length=50)

class User(AbstractUser):
    photo = models.ImageField(upload_to='user_images')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20, validators=[validate_password])

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    passport = models.FileField()
    CV = models.FileField()
    military_ID = models.FileField()
    reference = models.FileField()
    diplom = models.FileField()
    driving_license = models.FileField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-time_created',)

class Additional_document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-time_created',)
