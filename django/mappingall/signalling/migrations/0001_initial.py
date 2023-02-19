# Generated by Django 3.2.7 on 2021-09-23 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='emp_name')),
                ('age', models.IntegerField(verbose_name='emp_age')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30, verbose_name='emp_city')),
                ('state', models.CharField(max_length=30, verbose_name='emp_state')),
                ('empref', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adrref', to='signalling.emp')),
            ],
        ),
    ]