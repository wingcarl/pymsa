# Generated by Django 2.1 on 2018-08-17 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20180813_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='WindScrapy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wind_level', models.CharField(max_length=256)),
                ('add_time', models.DateTimeField()),
            ],
        ),
    ]
