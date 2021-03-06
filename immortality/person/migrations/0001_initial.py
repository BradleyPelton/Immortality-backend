# Generated by Django 3.0.6 on 2020-05-28 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('city_of_birth', models.CharField(blank=True, max_length=100)),
                ('country_of_birth', models.CharField(blank=True, max_length=100)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
