# Generated by Django 3.2.5 on 2021-08-03 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=100)),
                ('restaurant_location', models.CharField(max_length=100)),
                ('restaurant_contact_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('price', models.FloatField()),
                ('res_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodApp.restaurant')),
            ],
        ),
    ]
