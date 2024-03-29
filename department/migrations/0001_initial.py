# Generated by Django 2.1.7 on 2019-02-25 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('clas', models.CharField(max_length=35)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=35)),
                ('mobile', models.BigIntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=35)),
                ('mobile', models.BigIntegerField(max_length=100)),
            ],
        ),
    ]
