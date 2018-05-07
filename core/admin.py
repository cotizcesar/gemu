from django.contrib import admin

# Core: Importing Models
from .models import UProfile
from .models import Post

admin.site.register(UProfile)
admin.site.register(Post)