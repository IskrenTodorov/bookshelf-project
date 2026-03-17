from django import template

register = template.Library()


@register.filter(name='star_rating')
def star_rating(value):
    try:
        value = int(value)
        return '★' * value + '☆' * (5 - value)
    except (TypeError, ValueError):
        return '☆☆☆☆☆'


@register.filter(name='truncate_words_custom')
def truncate_words_custom(value, num):
    """Съкращава текст до N думи"""
    words = value.split()
    if len(words) > num:
        return ' '.join(words[:num]) + '...'
    return value


@register.simple_tag
def rating_color(rating):
    if rating >= 4:
        return 'text-success'
    elif rating >= 3:
        return 'text-warning'
    return 'text-danger'