from django.db import models


class Contract(models.Model):
    field = models.CharField(max_length=30)
