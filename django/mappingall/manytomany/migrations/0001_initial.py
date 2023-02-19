# Generated by Django 3.2.7 on 2021-09-22 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30, verbose_name='emp_city')),
                ('state', models.CharField(max_length=30, verbose_name='emp_state')),
                ('pin', models.IntegerField(verbose_name='emp_pincode')),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='emp_name')),
                ('age', models.IntegerField(verbose_name='emp_age')),
                ('salary', models.FloatField(verbose_name='emp_sal')),
                ('adrrefs', models.ManyToManyField(null=True, related_name='emprefs', to='manytomany.Address')),
            ],
        ),
    ]