# Generated by Django 3.1.1 on 2021-09-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
    ]