from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Index


class Country(models.Model):
    name = models.CharField(max_length=32, unique=True)
    Code = models.CharField(max_length=10, null=True, unique=True)

    class Meta:
        indexes = [
            Index(fields=('name',))
        ]
        verbose_name = _('Contry')
        verbose_name_plural = _('Countries')

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=40)
    country = models.ForeignKey(to='Country', on_delete=models.SET_NULL, null=True, related_name='cities')

    class Meta:
        indexes = [
            Index(fields=('name',)),
        ]
        verbose_name = _('Сity')
        verbose_name_plural = _('Сities')

    def __str__(self):
        return self.name


class Dealer(User):
    user = models.OneToOneField(User, parent_link=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    city = models.ForeignKey(to='City', on_delete=models.SET_NULL, null=True, blank=False)

    class Meta:
        verbose_name = _('Dealer')
        verbose_name_plural = _('Dealers')

        indexes = [
            Index(fields=['user', ])
        ]

    @property
    def title(self):
        return f'{self.get_full_name()}, from: {self.city.name}, email: {self.email}'

    def __str__(self):
        return self.title
