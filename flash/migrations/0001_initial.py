# Generated by Django 3.1 on 2020-08-16 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]
