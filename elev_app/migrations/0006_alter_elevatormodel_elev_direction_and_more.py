# Generated by Django 4.2.3 on 2023-07-29 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elev_app', '0005_delete_elevatorsystemmodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elevatormodel',
            name='elev_direction',
            field=models.CharField(choices=[('Up', 'Up'), ('Down', 'Down'), ('Stopped', 'Stopped')], default='Stopped', max_length=7),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='floor_direction',
            field=models.CharField(choices=[('Up', 'Up'), ('Down', 'Down'), ('Stopped', 'Stopped')], default='Stopped', max_length=7),
        ),
    ]