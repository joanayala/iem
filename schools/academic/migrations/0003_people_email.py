# Generated by Django 3.2.6 on 2021-09-29 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_people_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
    ]