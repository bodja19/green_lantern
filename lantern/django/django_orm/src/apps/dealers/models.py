from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Index


class DealerCountry(models.Model):
    name = models.CharField(max_length=32, unique=True)
    Code = models.IntegerField(max_length=10, null=True, unique=True)

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=('name',))
        ]
        verbose_name = _('Contry')
        verbose_name_plural = _('Country')

    def __str__(self):
        return self.name


class DealerCity(models.Model):
    name = models.CharField(Dealer=40)
    country = models.ForeignKey(DealerCountry, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=('name',)),
        ]
        verbose_name = _('Car model')
        verbose_name_plural = _('Car models')

    def __str__(self):
        return self.name

class Dealer(models.Model):
    title = models.CharField(max_length=64)
    email = models.EmailField(max_length=40, null=True, unique=True)
    city = model = models.ForeignKey(to='DealerCity', on_delete=models.SET_NULL, null=True, blank=False)

