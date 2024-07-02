from django import template
import markdown as md

register = template.Library()


@register.filter(name='markdown')
def markdown_format(text):
    return md.markdown(text, extensions=['markdown.extensions.fenced_code', 'markdown.extensions.nl2br'])
