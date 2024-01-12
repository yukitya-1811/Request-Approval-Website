# Generated by Django 4.2.7 on 2024-01-12 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('approvals', '0006_alter_request_template_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('0', 'Waiting for approval'), ('1', 'Approved by MIS Officer'), ('2', 'Approved by Head of Department'), ('3', 'Approved by Dean')], max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('MIS', 'MIS Officer'), ('HOD', 'Head of Department'), ('DEAN', 'Dean')], max_length=20, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
