from django.shortcuts import render, redirect, get_object_or_404
import random
from .models import Player, Game
from .forms import NameForm, LimitNumber, GuessNumber


def show_home(request):
    number = random.randint(0, 100)
    content = {
        'number': number,
        'have_games': Game.objects.all()
    }
    if request.session.get('player_id'):
        player = Player.objects.get(id=request.session.get('player_id'))
        if not player.name:
            content['name_form'] = NameForm
        if request.session.get('game_id'):
            return redirect(f'/game/{request.session.get("game_id")}/')
        else:
            list_game_player = []
            for game in Game.objects.all():
                if player.id in game.players.all() and game.status:
                    list_game_player.append(game.id)
            if list_game_player:
                content['list_game_player'] = list_game_player
    else:
        player = Player.objects.create()
        content['player'] = player
        if not player.name:
            content['name_form'] = NameForm
        player_id = player.id
        request.session['player_id'] = player_id
    return render(request, 'home.html', content)


def new_game(request):
    template = 'new_game.html'
    player_id = request.session['player_id']
    player = Player.objects.get(id=player_id)
    form = LimitNumber
    content = {
        'form': form,
    }
    if request.method == "POST":
        form = LimitNumber(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data['limit_number']
            game = Game.objects.create(
                hidden_number=random.randint(0, cleaned_data),
                top_count=cleaned_data,
                game_master=player.id
            )
            request.session['game_id'] = game.id
            game.players.add(player)
            player.game_master = True
            return redirect(f'/game/{game.id}/')
    return render(request, template, content)


def the_game(request, ig):
    template = 'game.html'
    game = get_object_or_404(Game, id=ig)
    print(game.hidden_number)
    request.session['game_id'] = game.id
    player_id = request.session['player_id']
    player = Player.objects.get(id=player_id)
    content = {
        'game': game,
        'player': player,
        'guess_form': GuessNumber
    }
    if game.game_master == player.id:
        content['count_players'] = len(game.players.all())
    if request.method == 'POST':
        form = GuessNumber(request.POST)
        if form.is_valid():
            player.count += 1
            player.save()
            guess_number = form.cleaned_data['guess_number']
            if guess_number == game.hidden_number:
                game.winner = player.id
                game.winner_count = player.count
                game.status = False
                game.save()
                player.count = 0
                player.save()
                request.session['game_id'] = None
            if (guess_number < game.hidden_number and guess_number > game.bottom_count):
                game.bottom_count = guess_number
                game.save()
            if (guess_number > game.hidden_number and guess_number < game.top_count):
                game.top_count = guess_number
                game.save()
    return render(request, template, content)