# Generated by Django 4.1.5 on 2023-01-24 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('nim', models.IntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=20)),
                ('alamat', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
