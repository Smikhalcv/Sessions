from django.db import models

from game.validator import validate_bigger_zero


class Player(models.Model):
    name = models.CharField(max_length=70, blank=True)
    count = models.IntegerField(default=0)


class Game(models.Model):
    hidden_number = models.IntegerField(validators=[validate_bigger_zero])
    players = models.ManyToManyField(Player, related_name='games', through='PlayerGameInfo')
    status = models.BooleanField(default=True)  # идёт игра или нет
    top_count = models.IntegerField()  # верхний предел
    bottom_count = models.IntegerField(default=0)  # нижний предел
    game_master = models.IntegerField()
    winner = models.IntegerField(blank=True, null=True)
    winner_count = models.IntegerField(blank=True, null=True)


class PlayerGameInfo(models.Model):
    players_in_game = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
