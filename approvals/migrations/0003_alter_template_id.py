# Generated by Django 4.2.7 on 2024-01-11 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approvals', '0002_alter_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
