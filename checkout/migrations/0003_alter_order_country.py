# Generated by Django 4.1.4 on 2023-01-12 08:37

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(default='IE', max_length=2),
        ),
    ]
