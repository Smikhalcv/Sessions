from django import forms
from django.core.exceptions import ValidationError

from .models import Player, Game
from .validator import validate_bigger_zero


class NameForm(forms.ModelForm):
    name = forms.CharField(max_length=70, label='Имя игрока')

    class Meta(object):
        model = Player
        fields = ('name',)

class LimitNumber(forms.Form):
    limit_number = forms.IntegerField(
        label='Максимальное число',
        validators=[validate_bigger_zero],
    )

class GuessNumber(forms.Form):
    guess_number = forms.IntegerField(
        label='Угадайте число',
        validators=[validate_bigger_zero],
    )