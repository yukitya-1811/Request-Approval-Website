# Generated by Django 4.2.7 on 2024-01-13 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('approvals', '0008_alter_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='template_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='approvals.template'),
        ),
    ]
