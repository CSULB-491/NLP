from django import template
from ..models import RSSFeed

register = template.Library()

@register.simple_tag
def get_rss_list():
    return {'rss_list': RSSFeed.objects.all()}

