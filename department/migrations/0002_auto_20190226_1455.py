# Generated by Django 2.1.7 on 2019-02-26 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='mobile',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
