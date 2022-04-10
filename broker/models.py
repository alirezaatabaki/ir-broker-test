from django.db import models
from django_jalali.db import models as jmodels


class Transaction(models.Model):
    BRANCH_CHOICES = [
        ('100', 'شعبه ۱۰۰'),
        ('101', 'شعبه ۱۰۱'),
        ('102', 'شعبه ۱۰۲'),
    ]

    national_id = models.CharField(max_length=10, verbose_name='کد ملی')
    branch = models.CharField(max_length=3, choices=BRANCH_CHOICES, verbose_name='کد شعبه')
    transaction_value = models.PositiveIntegerField(verbose_name='ارزش معامله')
    created = jmodels.jDateTimeField(auto_now_add=True)
