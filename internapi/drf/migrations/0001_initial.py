# Generated by Django 4.0.3 on 2022-04-09 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(blank=True, max_length=100)),
                ('attandence', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
