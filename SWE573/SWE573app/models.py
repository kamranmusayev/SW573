from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class User_profile(models.Model):
    _id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    username = models.CharField(default=0, max_length=200)
    email = models.EmailField(max_length=100, blank=False)
    bio = models.TextField()

    @classmethod
    def create(cls, user): 
        profile = cls(_id= user, name= (user.first_name+" "+user.last_name),username=user.username, email=user.email)

        return profile


    def __str__(self):
        return self.username


class Post(models.Model):
    _id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    post_data = models.TextField()
    date = models.DateField()
    place = models.CharField(max_length=50)

    def __str__(self):
        return self.title


