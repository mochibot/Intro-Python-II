# Add an Item class in here. The item should have name and description attributes.

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f'You have picked up {self.name}')
    
    def on_drop(self):
        print(f'You have dropped {self.name}')