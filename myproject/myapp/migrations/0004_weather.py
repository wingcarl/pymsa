# Generated by Django 2.1 on 2018-08-13 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_water'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather_detail', models.CharField(max_length=1024)),
                ('add_time', models.DateTimeField()),
            ],
        ),
    ]