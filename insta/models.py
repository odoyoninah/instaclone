from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile_(self, new_profile):
        self.profile = new_profile
        self.save()



    def __str__(self):
        return self.user.username


class Image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    caption = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    comments = models.CharField(max_length=100,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self,new_caption):
        self.image_caption = new_caption
        self.save()

    def __str__(self):
        return self.caption

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def update_comment(self, new_comment):
        self.comment = new_comment
        self.save()


    def __str__(self):
        return self.comment

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)

    def save_like(self):
        self.save()

    def delete_like(self):
        self.delete()

    def update_like(self, new_like):
        self.like = new_like
        self.save()

    def __str__(self):
        return self.user.username

class Follow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    follower = models.ForeignKey(User,related_name='follower',on_delete=models.CASCADE)

    def save_follow(self):
        self.save()

    def delete_follow(self):
        self.delete()

    def update_follow(self, new_follow):
        self.follow = new_follow
        self.save()

    def __str__(self):
        return self.user.username
    