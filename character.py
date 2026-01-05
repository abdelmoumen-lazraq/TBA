
from room import Room
import random as random

class Character:

    # DEBUG = None
    def __init__(self, name, description, current_room):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = {}
    
    def __str__(self):
        return  self.name \
                + " : " \
                + self.description
    
    def move(self):
        current_room = self.current_room
        a = random.choice([1,2])
        print(a)
        from game import DEBUG
        if a == 1:
            if DEBUG:
                print(f"DEBUG : {self.name} n'a pas bougé et se trouve dans la zone '{self.current_room.name}'\n")
            return False

        else:
            liste_sorties = []
            for i in current_room.exits.keys():
                liste_sorties.append(current_room.exits[i])

            print(liste_sorties)
            next_room = random.choice(liste_sorties)
            current_room = next_room
            if DEBUG:
                print(f"DEBUG : {self.name} se trouve dans la zone '{self.current_room.name}'\n")
            return True

