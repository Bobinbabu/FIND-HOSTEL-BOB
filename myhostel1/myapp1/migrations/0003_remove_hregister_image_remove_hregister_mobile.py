# Generated by Django 4.1.7 on 2023-06-02 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_hlogin_hregister'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hregister',
            name='image',
        ),
        migrations.RemoveField(
            model_name='hregister',
            name='mobile',
        ),
    ]