# Generated by Django 4.2.7 on 2024-01-25 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angara_vehicles_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
