# Generated by Django 4.1.dev20220328112539 on 2022-04-08 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('usename', models.CharField(max_length=200)),
                ('pwd', models.CharField(max_length=200)),
            ],
        ),
    ]