# Generated by Django 5.0.3 on 2024-03-20 23:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_modulo_delete_barcode_delete_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soilhumsens', models.DecimalField(decimal_places=2, max_digits=10)),
                ('humsens', models.DecimalField(decimal_places=2, max_digits=10)),
                ('temp', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Modulo',
        ),
        migrations.AddField(
            model_name='module',
            name='Sensors',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sensor'),
        ),
    ]