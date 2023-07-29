# Generated by Django 4.2.3 on 2023-07-29 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elev_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_number', models.IntegerField()),
                ('floor_direction', models.CharField(choices=[('U', 'Upward'), ('D', 'Downward'), ('S', 'Stopped')], default='S', max_length=1)),
                ('destination_floor', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
