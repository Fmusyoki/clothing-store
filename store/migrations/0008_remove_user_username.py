# Generated by Django 4.2.1 on 2023-07-11 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Username',
        ),
    ]