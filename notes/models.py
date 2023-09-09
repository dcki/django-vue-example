from django.db import models


class Note(models.Model):
    content = models.CharField(max_length=50)
