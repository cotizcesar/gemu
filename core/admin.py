from django.contrib import admin

# Core: Importing Models
from .models import UserProfile, Connection, Post

admin.site.register(UserProfile)
admin.site.register(Connection)
admin.site.register(Post)