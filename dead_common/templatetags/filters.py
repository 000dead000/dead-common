from django.template.defaultfilters import register


@register.filter(name='get_value')
def get_value(dictionary, key):
    return dictionary.get(key)
