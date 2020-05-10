from django.db import models
from django.utils import timezone
# Create your models here.
class post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True)
    caption=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.caption
class User(models.Model):
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=140)
    password=models.CharField(max_length=100)
    last_login=models.DateTimeField(auto_now=True)