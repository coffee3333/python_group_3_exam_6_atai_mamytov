# Generated by Django 2.2 on 2019-09-21 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_author', models.CharField(max_length=3500, verbose_name='Name')),
                ('mail_author', models.CharField(max_length=3500, verbose_name='Mail')),
                ('entry', models.TextField(max_length=3500, verbose_name='Entry')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Date of create')),
                ('changed_at', models.DateField(auto_now=True, verbose_name='Date of change')),
                ('status', models.TextField(choices=[('Active', 'active'), ('Blocked', 'blocked')], default='active', max_length=50, verbose_name='Status')),
            ],
        ),
    ]
