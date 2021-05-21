from django.db import models
from django.utils import timezone


class Test(models.Model):
    name = models.CharField(
        default=f"test_{timezone.now().strftime('%Y%m%d')}",
        max_length=30
    )

    description = models.CharField(
        default='',
        max_length=100
    )

    timestamp = models.DateTimeField(
        auto_now=True
    )

    STATUSES = (
        ('0', 'Success'),
        ('1', 'Failure')
    )

    status = models.CharField(
        default=STATUSES[0][0],
        max_length=10,
        choices=STATUSES
    )

    def __str__(self):
        return self.name