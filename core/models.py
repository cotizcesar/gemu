from django.db import models

# Django: Importing User Model
from django.contrib.auth.models import User

# Core: UProfile reciever and post_save signal: Needed to create a UProfile objects when the User account its created.
from django.dispatch import receiver
from django.db.models.signals import post_save

class UProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user/avatar', default='avatar/default.png', blank=True)
    header = models.ImageField(upload_to='user/header', default='avatar/default.png', blank=True)
    bio = models.CharField(max_length=140, blank=True)
    website = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UProfile.objects.create(user=instance)
    instance.uprofile.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.uprofile.save()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=280)
    image = models.ImageField(upload_to='post/image', blank=True)
    video = models.URLField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_created"]
    
    def __str__(self):
        return "{} {} (@{}) : {}".format(self.user.first_name, self.user.last_name, self.user.username, self.text)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.text