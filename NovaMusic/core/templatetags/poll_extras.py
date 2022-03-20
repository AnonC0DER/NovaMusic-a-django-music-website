from django import template
from textwrap import wrap
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='charwrap')
@stringfilter
def charwrap(text, width=50):
    '''Wraps character at specified line length'''
    return ' '.join(wrap(text, width))