class Monster:
    def __init__(self, name, hp = 100):
        self.name = name
        self.hp = hp
    
    def attack(self, player):
        player.hp -=  30

    def on_attack(self):
        self.hp = 0
        print(f'{self.name} was defeated')