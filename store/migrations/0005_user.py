# Generated by Django 4.2.1 on 2023-07-06 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_trending'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('ConfirmPassword', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
    ]
