from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.
class Questions(models.Model):
    content=models.TextField(null=False)
    def __str__(self):
        return self.content

class User(AbstractUser):

    """User Model"""
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified')
    )
    # First Name and Last Name do not cover name patterns
    # around the globe.
    profile_image = models.ImageField(null=True)
    name = models.CharField(blank=True, max_length=255)
    website = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=140, blank=True, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

class Post(models.Model):

    pub_date = models.DateTimeField('data published')
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.answer

    # class Meta:
    #     # 생성된 날짜순으로 정령
    #     ordering = ['-created_at']


class Comment(models.Model):

    message = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name="comment_user")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Like(models.Model):
    creator = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name="like_post")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)