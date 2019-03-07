from django import template
from django.shortcuts import render_to_response
from django.template import RequestContext

from question import models

register = template.Library()

@register.inclusion_tag('profile.html')
def recently_post(is_safe=True):
    questions = models.Questions.objects.all()[:5]
    posts = models.Post.objects.all()[:5]
    return {'questions': questions, 'posts': posts}
