import time


class Room:
    def __init__(self, _id):
        self._id = _id
        self.last_active = time.time()
        self.players = []
        self.status = None

    def keep_active(self):
        self.last_active = time.time()


class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.last_active = time.time()
        self.room_id = None
        self.name = None
        self.role = None

    def keep_active(self):
        self.last_active = time.time()
