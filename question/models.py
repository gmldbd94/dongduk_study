from django.db import models
import getpass

# Create your models here.

class Questions(models.Model):
    content=models.TextField(null=False)

class Post(models.Model):
    question=
    answer=models.TextField(null=False)
    author=getpass.getuser()