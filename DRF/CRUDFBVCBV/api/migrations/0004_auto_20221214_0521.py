# Generated by Django 2.2.7 on 2022-12-13 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_student_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created_by',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]