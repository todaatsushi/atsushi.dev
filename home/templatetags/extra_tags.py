from django import template


register = template.Library()


@register.filter
def add_class(value, arg):
    """
    Adds arg class(es) to value.
    """
    return value.as_widget(attrs={
        'class': arg
    })


@register.filter
def loop_nums(min=5):
    """
    Range filter for numerical loops.
    """
    return range(1, min + 1)


@register.filter
def replace_space(value, arg="-"):
    """
    Replace spaces with arg.
    """
    return value.replace(" ", arg)


@register.filter
def split_commas(value):
    """
    Splits comma separated values into a list.
    """
    return value.split(',')
