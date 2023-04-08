# Generated by Django 3.2.7 on 2021-09-15 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photoidproof', models.CharField(max_length=60)),
                ('idnumber', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=60)),
                ('gender', models.CharField(max_length=60)),
                ('dateofbirth', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'register',
            },
        ),
        migrations.CreateModel(
            name='Slotbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointmentfor', models.CharField(max_length=60)),
                ('date', models.CharField(max_length=60)),
                ('time', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'slotbooking',
            },
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
