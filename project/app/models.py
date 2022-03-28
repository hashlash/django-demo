from django.db import models
from django.utils.html import format_html, format_html_join


class ExampleModel(models.Model):
    field = models.TextField()
