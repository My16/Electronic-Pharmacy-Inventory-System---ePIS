# yourapp/templatetags/app_extras.py
# ─────────────────────────────────────────────────────────────────────────────
# Custom template tags used across the system.
# ─────────────────────────────────────────────────────────────────────────────
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def url_replace(context, field, value):
    """
    Returns the current query string with one parameter replaced/added.
    Usage in template:  href="?{% url_replace request 'page' num %}"
    """
    request     = context['request']
    dict_       = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()