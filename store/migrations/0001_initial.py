# Generated by Django 4.2.1 on 2023-06-20 12:18

from django.db import migrations, models
import django.db.models.deletion
import store.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path)),
                ('trending', models.BooleanField(default=False, help_text='0=default, 1=Trending')),
                ('new_arrivals', models.BooleanField(default=False, help_text='0=default, 1=new_arrivals')),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_keywords', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path)),
                ('quantity', models.IntegerField()),
                ('Selling_price', models.FloatField()),
                ('trending', models.BooleanField(default=False, help_text='0=default, 1=Trending')),
                ('new_arrivals', models.BooleanField(default=False, help_text='0=default, 1=new_arrivals')),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_keywords', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
    ]
