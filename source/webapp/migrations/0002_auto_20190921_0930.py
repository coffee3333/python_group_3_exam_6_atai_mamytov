# Generated by Django 2.2 on 2019-09-21 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='status',
            field=models.TextField(choices=[('active', 'active'), ('blocked', 'blocked')], default='active', max_length=50, verbose_name='Status'),
        ),
    ]
