# Generated by Django 2.2.10 on 2020-09-30 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hidden_number', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('top_count', models.IntegerField()),
                ('bottom_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_master', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=70)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerGameInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Game')),
                ('players_in_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Player')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(related_name='players', through='game.PlayerGameInfo', to='game.Player'),
        ),
    ]
