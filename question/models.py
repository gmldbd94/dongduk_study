from django.db import models

# Create your models here.

class Questions(models.Model):
    content=models.TextField()

class Post(models.Model):
    #question=
    pub_date=models.DateTimeField('data published')
    #answer=
    #author=