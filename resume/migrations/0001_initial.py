# Generated by Django 5.1.3 on 2024-12-17 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(blank=True, max_length=50, null=True)),
                ('userNumber', models.CharField(blank=True, max_length=10, null=True)),
                ('admin', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
