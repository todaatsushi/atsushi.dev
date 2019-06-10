from django import template

import re


register = template.Library()


@register.filter
def add_class_form(value, arg):
    """
    Adds arg class(es) to value (only for forms).
    """
    return value.as_widget(attrs={
        'class': arg
    })


@register.filter(is_safe=True)
def add_class(value, arg):
    """
    Adds arg class(es) to value (non form elements).
    """
    vals = value.split('\n')
    final = ''

    for val in vals:
        # make sure list item is not blank
        if val is not "":
            i = val.find('>')
            
            # insert class arg between end of tag and close of tag
            new = val[0:i] + f' class="{arg}"' + val[i:len(val)]
            final += new
    return final

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
