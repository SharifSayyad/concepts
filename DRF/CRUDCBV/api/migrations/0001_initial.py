# Generated by Django 2.2.7 on 2022-11-26 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('roll', models.IntegerField()),
                ('city', models.CharField(max_length=30)),
            ],
        ),
    ]
