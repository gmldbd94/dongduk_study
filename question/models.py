from django.db import models


# Create your models here.

class Questions(models.Model):
    content=models.TextField(null=False)

class Post(models.Model):

    pub_date=models.DateTimeField('data published')
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer=models.TextField(null=False)
    author=models.TextField(null=False) # 현재 사용중인 user 반환하여 views.py에서 str

