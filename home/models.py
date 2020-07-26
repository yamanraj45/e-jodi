from django.db import models
from django.contrib.auth.models import User


from django.conf import settings

class Gender(models.Model):
    gender = models.CharField(max_length=20)
    def __str__(self):
        return self.gender
    


class UserProfile(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="gallery")
    bio = models.CharField(max_length=150)
    location = models.CharField(max_length=200)
    hobby = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user.username
    


class Like(models.Model):
    liked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    liked_to : models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return '%s Liked %s'%(self.liked_by, self.liked_to)

    


class Ignore(models.Model):
    ignored_by: models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ignored_to: models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return '%s Ignored %s'%(self.ignored_by, self.ignored_to)