from django.db import models
from common.models import BaseDateAuditModel
from django.db.models import Index
from django.utils.translation import gettext_lazy as _
# Create your models here.
from apps.orders.manager import OrderManager, OrderQuerySet


class Order(BaseDateAuditModel):
    STATUS_PENDING = 'pending'
    STATUS_PENDING_PAYMENT = 'pend_pay'
    STATUS_PEID = 'paid'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_PENDING_PAYMENT, "Pendind payment"),
        (STATUS_PEID, "Paid"),
        (STATUS_ARCHIVED, "Archived"),
    )

    objects = OrderManager.from_queryset(OrderQuerySet)()

    first_name = models.CharField(max_length=32, unique=True)
    last_name = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=40, unique=True)
    phone = models.IntegerField(max_length=15, null=False, blank=True, unique=True)
    message = models.TextField(max_length=500, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING, blank=True)
    car = models.ManyToManyField(to='cars.Car', related_name='orders')

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

        indexes = [
            Index(fields=['last_name', 'email'])
        ]

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name