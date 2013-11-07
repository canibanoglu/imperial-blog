from django import template
from django.template.defaultfilters import stringfilter
import markdown

register = template.Library()

@register.filter(name='mdbody')
@stringfilter
def mdbody(value):
    """Return the HTML output from the markdown library"""
    return markdown.markdown(value, extensions=['fenced_code'], safe_mode='escape')

@register.filter(name='mdparagraph')
@stringfilter
def mdparagraph(value):
    """Returns the HTML output for the first paragraph
    of the value from the markdown library"""
    first_paragraph = value.split('\r\n\r\n', 2)[0]
    return markdown.markdown(first_paragraph, extensions=['fenced_code'], safe_mode='escape')
