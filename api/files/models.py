import uuid

from django.db import models
from django.utils import timezone


class FileInfo(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    size = models.IntegerField()
    upload_date = models.DateTimeField(default=timezone.now, editable=False)
    file = models.FileField(upload_to='public', null=True)

    class Meta:

        verbose_name = 'File info'
        verbose_name_plural = 'File infos'
