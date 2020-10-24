import random
import time

from django.http import HttpResponse
from django.shortcuts import render

from .models import Room, Player

MAX_ROOMS = 100
ROOM_TIMEOUT = 3600
ROOM_MIN_PLAYER = 5
ROOM_MAX_PLAYER = 10
MAX_PLAYERS = MAX_ROOMS * ROOM_MAX_PLAYER
PLAYER_TIMEOUT = 1800
COOKIES_PLAYER_ID = 'player_id'
SESSION_ID = 'sessionid'

rooms = {}
players = {}
sessions = {}


def generate_id():
    return str(random.randint(10000, 99999))


def get_player(request):
    player = None
    if 'player_id' in request.session:
        player_id = request.session['player_id']
        if player_id is not None:
            if player_id in players:
                player = players[player_id]
                player.keep_active()
    return player


def create_player():
    player = None
    if len(players) < MAX_PLAYERS:
        player_id = generate_id()
        while player_id in players:
            player_id = generate_id()
        player = Player(player_id)
        players.update({player_id: player})
    return player


def clear():
    current_time = time.time()
    for room in rooms:
        alive_time = current_time - room.start_time
        if alive_time > ROOM_TIMEOUT:
            rooms.pop(room)
    for player in players:
        alive_time = current_time - player.last_active_time
        if alive_time > PLAYER_TIMEOUT:
            players.pop(player)


def create_room(request):
    clear()
    room_id = generate_id()
    while room_id in rooms:
        room_id = generate_id()
    room = Room(room_id)

    player = get_player(request)
    if player is None:
        player = create_player()
        if player is None:
            print('max number of player per server')
        else:
            print('todo store cookies')

    if len(room) < MAX_ROOMS:
        player.room_id = room_id
        players.update(player.player_id, player)## check if this is needed

        room.status = 'CREATED'
        room.players.append(player)
        rooms.update(room.room_id, room)
    else:
        print('max room')


def join_room(request, room_id):
    if room_id in rooms:
        room = rooms[room_id]
        if len(room.players) < ROOM_MAX_PLAYER:
            player = get_player(request)
            player.room_id(room_id)
            room.players.append(player)
        else:
            print('max player for room')
    else:
        print('room not exist')


def room(request):
    player = get_player(request)
    room = rooms[player.room_id]
    print('l4s:')


def lobby(request):
    player = get_player(request)

    response = render(request, 'rooms/lobby.html', {'player': player})

    if player is None:
        player = create_player()
        request.session['player_id'] = player.player_id
        #sessions.update({str(request.COOKIES.get(SESSION_ID)): player.player_id})
    return response


def waiting_room(request):
    player = get_player(request)
    return render(request, 'rooms/waiting_room.html', {'player': player})


