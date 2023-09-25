from django import template

register = template.Library()


@register.filter
def break_at_condition(value, condition):
    for item in value:
        if condition != item.created_by:
            return item.created_by.username
    return None


register.filter('modify_content', break_at_condition)
