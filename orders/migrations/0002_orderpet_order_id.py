# Generated by Django 4.2.1 on 2023-08-24 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderpet',
            name='order_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='orders.orders'),
        ),
    ]