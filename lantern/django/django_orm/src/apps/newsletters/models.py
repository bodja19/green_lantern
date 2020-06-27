from django.db import models
from common.models import BaseDateAuditModel
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Newsletter(BaseDateAuditModel):
    email = models.EmailField(max_length=32, null=True, unique=True)

    class Meta:
        verbose_name = _('Newsletter')
        verbose_name_plural = _('Newsletters')

    def __str__(self):
        return self.email
