# Generated by Django 2.1.7 on 2019-03-25 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Event Name')),
                ('event_date', models.DateTimeField(verbose_name='Event Date')),
                ('venue', models.CharField(max_length=120)),
                ('manager', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
