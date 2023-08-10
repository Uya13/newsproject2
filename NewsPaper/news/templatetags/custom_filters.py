from django import template
import re

register = template.Library()

censu = ['редиска', 'собака', 'псина', 'блин']


@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise TypeError()

    for word in re.findall(r"[\w']+|[.,!?;]",value):
        if word.lower() in censu:
            value = value.replace(word, f"{word[0]}{'*'*(len(word)-2)}{word[-1]}")
    return value

