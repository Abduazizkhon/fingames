# Generated by Django 5.1 on 2024-10-31 21:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0005_game_download_count"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="game",
            name="playernum",
        ),
        migrations.RemoveField(
            model_name="game",
            name="time",
        ),
        migrations.AddField(
            model_name="game",
            name="lowplayernum",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="game",
            name="lowtime",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="game",
            name="upplayernum",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="game",
            name="uptime",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
