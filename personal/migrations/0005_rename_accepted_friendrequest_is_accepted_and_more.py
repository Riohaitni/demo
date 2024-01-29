# Generated by Django 5.0.1 on 2024-01-29 08:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_remove_friendinvitation_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendrequest',
            old_name='accepted',
            new_name='is_accepted',
        ),
        migrations.RenameField(
            model_name='friendrequest',
            old_name='created_at',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='friendrequest',
            name='current_time',
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]
