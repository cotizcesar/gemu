from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Avatar and Header ImageField's Processing
from PIL import Image
from PIL import ImageOps
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', default='avatar/default.png')
    header = models.ImageField(upload_to='header', default='header/default.png')
    bio = models.TextField(max_length=140, blank=True)
    website = models.URLField(max_length=200, blank=True)
    location = models.CharField(max_length=30, blank=True)
    date_birth = models.DateField(null=True, blank=True)
    """
    def save(self):
        if self.avatar:
            # Open image from avatar ImageField.
            im = Image.open(self.avatar)
            output = BytesIO()

            # Resize image to 200x200 maintaining aspect ratio with Antialias for better quality.
            im = ImageOps.fit(im, (200,200), method=Image.ANTIALIAS, bleed=0.0, centering=(0.5, 0.5))

            # Change file color to RGB.
            im = im.convert('RGB')

            # After modifications, save it to the output with 100% of quality.
            im.save(output, format='JPEG', quality=100)
            output.seek(0)

            # Change the imagefield value to be the new modifed image value.
            self.avatar = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.avatar.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        if self.header:
            # Open image from avatar ImageField.
            im = Image.open(self.header)
            output = BytesIO()

            # Resize image to 200x200 maintaining aspect ratio with Antialias for better quality.
            im = ImageOps.fit(im, (1170,350), method=Image.ANTIALIAS, bleed=0.0, centering=(0.5, 0.5))

            # Change file color to RGB.
            im = im.convert('RGB')

            # After modifications, save it to the output with 100% of quality.
            im.save(output, format='JPEG', quality=100)
            output.seek(0)

            # Change the imagefield value to be the new modifed image value.
            self.header = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.header.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        else:

        super(UserProfile,self).save()
        """


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class Connection(models.Model):
    following = models.ForeignKey(User, related_name='following')
    follower = models.ForeignKey(User, related_name='follower')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} > {}".format(self.following.username, self.follower.username)