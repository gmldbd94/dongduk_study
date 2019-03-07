from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from .models import Questions, Post, Comment, Like, User

admin.site.register(Questions)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (("User", {"fields": ("name","profile_image")}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]
# # Register your models here.
