from django.contrib import admin
from .models import Connection, UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'date_birth',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Connection)