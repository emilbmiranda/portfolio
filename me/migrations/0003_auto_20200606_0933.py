# Generated by Django 3.0.7 on 2020-06-06 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0002_auto_20200606_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
