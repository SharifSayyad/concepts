# Generated by Django 2.2.7 on 2022-02-02 04:19

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='emp_name')),
                ('age', models.IntegerField(verbose_name='emp_age')),
                ('salary', models.FloatField(verbose_name='emp_sal')),
                ('email', models.EmailField(max_length=254, verbose_name='emp_email')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30, verbose_name='emp_city')),
                ('state', models.CharField(max_length=30, verbose_name='emp_state')),
                ('pin', models.IntegerField(verbose_name='emp_pincode')),
                ('empref', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adrref', to='endtoend.Emp')),
            ],
        ),
    ]
