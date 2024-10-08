# Generated by Django 5.1 on 2024-08-21 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("escola", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="curso",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="curso",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="estudante",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="estudante",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
    ]
