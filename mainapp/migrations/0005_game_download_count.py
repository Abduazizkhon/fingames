# Generated by Django 5.1 on 2024-10-05 14:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0004_mainintro"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="download_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
