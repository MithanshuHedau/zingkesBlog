from django.db import models
from datetime import datetime
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(blank=True, null=True)
