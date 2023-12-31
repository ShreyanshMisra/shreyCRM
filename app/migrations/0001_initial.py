# Generated by Django 4.2.2 on 2023-07-17 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('first', models.CharField(max_length=15)),
                ('last', models.CharField(max_length=15)),
                ('role', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('linkedin', models.URLField(max_length=300)),
                ('location', models.CharField(max_length=300)),
                ('notes', models.CharField(max_length=1000)),
            ],
        ),
    ]
