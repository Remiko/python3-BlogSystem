from django import template
from django.conf import settings
import os

register = template.Library()


@register.filter
def imgfilter(value):
    i = os.listdir(settings.BASE_DIR + '/static/images/categories/')
    for n in i:
        n_img = n.split('_')
        img = n_img[0].lower()
        if img == 'framework':
            img = '框架'
        elif img == 'leetcode':
            img = '刷一刷'
        elif img == 'life':
            img = '日常'
        if value.lower() == img:
            img = n_img[0] + '_' + n_img[1]
            return img


