# Generated by Django 2.2.7 on 2022-02-02 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onetomany', '0002_auto_20220202_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='empref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adrrefs', to='onetomany.Emp'),
        ),
    ]
