# Generated by Django 4.1.5 on 2023-02-03 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='email',
        ),
    ]