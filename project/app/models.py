from django.db import models
from django.utils.html import format_html, format_html_join


def list_help_text_html(help_texts):
    """
    Inspired from django.contrib.auth.password_validation._password_validators_help_text_html
    https://github.com/django/django/blob/d90e34c61b27fba2527834806639eebbcfab9631/django/contrib/auth/password_validation.py#L84-L93
    """
    help_items = format_html_join(
        "", "<li>{}</li>", ((help_text,) for help_text in help_texts)
    )
    return format_html("<ul>{}</ul>", help_items) if help_items else ""


class ExampleModel(models.Model):
    field = models.TextField(
        help_text=list_help_text_html([
            'info a',
            'info b',
        ]),
    )
