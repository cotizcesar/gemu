from django.contrib import admin

# Core: Importing Models
from .models import UserProfile
from .models import Post

admin.site.register(UserProfile)
admin.site.register(Post)