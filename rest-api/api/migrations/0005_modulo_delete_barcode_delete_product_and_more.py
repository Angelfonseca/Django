# Generated by Django 5.0.3 on 2024-03-20 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_barcode_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('soilhumsens', models.DecimalField(decimal_places=2, max_digits=10)),
                ('humsens', models.DecimalField(decimal_places=2, max_digits=10)),
                ('temp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Barcode',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.RemoveField(
            model_name='user',
            name='curp',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
    ]
