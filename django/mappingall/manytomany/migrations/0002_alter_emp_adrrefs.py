# Generated by Django 3.2.7 on 2021-09-22 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manytomany', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='adrrefs',
            field=models.ManyToManyField(related_name='emprefs', to='manytomany.Address'),
        ),
    ]
