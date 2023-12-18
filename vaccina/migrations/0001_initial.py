# Generated by Django 5.0 on 2023-12-18 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('dose_count', models.PositiveIntegerField()),
                ('release_year', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Вакцины',
            },
        ),
    ]
