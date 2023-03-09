from django.db import models
from consumers.models import Consumers
from core.models import TimeStampedModel


class SalesPlan(TimeStampedModel):
    consumer = models.ManyToManyField(Consumers, related_name='plans', verbose_name='مصرف کننده')
