# Generated by Django 2.1.5 on 2019-03-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employeer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('log_date', models.DateField(blank=True, null=True)),
                ('log_time', models.TimeField(blank=True, null=True)),
                ('login', models.TimeField(blank=True, null=True)),
                ('logout', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]
