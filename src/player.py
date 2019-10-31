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

        if moves[direction]:
            self.current_room = moves[direction]
            print(f'You are now in: {self.current_room.name}')
            print(self.current_room.description)
        else:
            print('Move is not allowed')
    
    def take(self, item):
        #note Item is not subscriptable
        new_item = next((d for d in self.current_room.items if d.name == item), None)     #returns the next item in the iterator or default value 
        
        if new_item:   
            new_item.on_take()
            self.items.append(new_item)
        else:
            print(f'{item} is not available in this room')
    
    def drop(self, item):
        discard_item = next((d for d in self.items if d.name == item), None) 

        if discard_item:
            discard_item.on_drop()
            self.items.remove(discard_item)
        else:
            print(f'{item} is not in your inventory')
    
    def show_items(self):
        if len(self.items) == 0:
            print('There is no items in your inventory')
        else:
            count = 1
            print('Here are your items:')
            for item in self.items:
                print(f'{count}. {item.name} - {item.description}')
                count += 1