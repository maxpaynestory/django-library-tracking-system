# Generated by Django 4.2 on 2025-03-20 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
