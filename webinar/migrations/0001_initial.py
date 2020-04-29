# Generated by Django 3.0.5 on 2020-04-29 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JustEdit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=4)),
                ('subject', models.CharField(max_length=100)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JustUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30, verbose_name='First Name')),
                ('lname', models.CharField(max_length=30, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('college', models.CharField(max_length=30, verbose_name='College/Organization')),
                ('profession', models.CharField(max_length=30, verbose_name='Profession')),
            ],
        ),
    ]
