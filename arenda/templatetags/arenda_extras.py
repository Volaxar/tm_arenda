from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
@stringfilter
def split_str(value):
    return mark_safe('<br>'.join(value.split(' ')))


@register.simple_tag
def get_cost(price, area):
    return '%.1f' % (price * area)


@register.simple_tag(takes_context=True)
def get_kind_icon(context):
    """
    Проверяет активен или нет тип объекта в фильтре

    Возвращает соответствующую иконку
    """
    kind = context['kind']
    filter_data = context['request'].session['filter']
    
    return kind.image_active if str(kind.id) in filter_data else kind.image
