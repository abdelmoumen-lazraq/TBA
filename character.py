import random
DEBUG = False

class Character:
    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs[:]  

    def __str__(self):
        return f"{self.name} : {self.description}"

    def move(self):
        """
        Déplace le PNJ avec une chance sur deux
        vers une salle adjacente choisie au hasard.
        """
        if random.choice([True, False]):
            possible_rooms = [
                room for room in self.current_room.exits.values()
                if room is not None
            ]

            if possible_rooms:
                old_room = self.current_room
                new_room = random.choice(possible_rooms)

                old_room.characters.remove(self)
                new_room.characters.append(self)
                self.current_room = new_room

                if DEBUG:
                    print(
                        f"[DEBUG] {self.name} s'est déplacé de "
                        f"{old_room.name} à {new_room.name}."
                    )

                return True
        return False
    def get_msg(self):
        """
        Retourne un message du PNJ de manière cyclique.
        """
        if not self.msgs:
            return ""

        msg = self.msgs.pop(0)
        self.msgs.append(msg)
        return msg
    #On peut fixer le message du PNJ à une condition spécifique puis le message va changer en fonction de cette condition.
    # Changer la salle initiale du joueur afin d'eviter de se déplacer à chaque test dès le début