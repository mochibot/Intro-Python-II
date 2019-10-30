# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move_room(self, direction):
        moves = {'n': self.current_room.n_to,
                 's': self.current_room.s_to,
                 'e': self.current_room.e_to,
                 'w': self.current_room.w_to}

        if moves[direction] != None:
            self.current_room = moves[direction]
        else:
            print('Move is not allowed')