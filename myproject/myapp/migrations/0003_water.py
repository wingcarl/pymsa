# Generated by Django 2.1 on 2018-08-10 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180809_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_high', models.CharField(max_length=64)),
                ('add_time', models.DateTimeField()),
            ],
        ),
    ]
