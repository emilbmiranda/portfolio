# Generated by Django 3.0.7 on 2020-06-06 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0009_auto_20200606_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill_type',
            field=models.CharField(choices=[('Programming Language', 'Programming Language'), ('Database', 'Database'), ('Integrated Development Environment/Text Editor', 'Integrated Development Environment/Text Editor'), ('Report/Analytics', 'Report/Analytics'), ('ETL', 'ETL'), ('Non-technical', 'Non-technical')], max_length=100),
        ),
    ]
