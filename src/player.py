# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def move_room(self, direction):
        moves = {'n': self.current_room.n_to,
                 's': self.current_room.s_to,
                 'e': self.current_room.e_to,
                 'w': self.current_room.w_to}

        if moves[direction] != None:
            self.current_room = moves[direction]
        else:
            print('Move is not allowed')
    
    def take(self, item):
        item.on_take()
        self.items.append(item)
    
    def drop(self, item):
        item.on_drop()
        self.items.remove(item)
    
    def show_items(self):
        if len(self.items) == 0:
            print('There is no items in your inventory')
        else:
            for item in self.items:
                print(item.name)