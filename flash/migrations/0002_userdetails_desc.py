# Generated by Django 3.1 on 2020-08-17 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='desc',
            field=models.TextField(default='we all are green arrow'),
            preserve_default=False,
        ),
    ]
