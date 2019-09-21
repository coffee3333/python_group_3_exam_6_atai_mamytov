from django.db import models

STATUS = [
    ('Active', 'active'),
    ('Blocked', 'blocked')
]

class Books(models.Model):
    name_author = models.CharField(max_length=3500, null=False, blank=False, verbose_name='Name')
    mail_author = models.CharField(max_length=3500, null=False, blank=False, verbose_name='Mail')
    entry = models.TextField(max_length=3500, null=False, blank=False, verbose_name='Entry')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date_of_create')
    changed_at = models.DateTimeField(auto_now=True, verbose_name='Date of change')
    status = models.TextField(max_length=50, null=False, blank=False, choices=STATUS, default='active', verbose_name='Status')
