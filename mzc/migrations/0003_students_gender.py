# Generated by Django 2.1.3 on 2019-10-01 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mzc', '0002_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('O', 'OTHER')], default='M', max_length=20),
        ),
    ]