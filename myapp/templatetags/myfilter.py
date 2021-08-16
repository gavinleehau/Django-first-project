from django import template

register=template.Library()

@register.filter
def make_range(number):
    return range(1, number + 1)