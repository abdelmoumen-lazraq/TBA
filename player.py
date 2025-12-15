# Define the Player class.

from room import Room

class Player():
    """
    This Class represents a player. A player is composed of a name and a current room where he is.

    Attributes:
        name (str): The name of the player.
        current_room (str): The room where the player is currently.
    
    Methods:
        __init__(self, name) : The constructor.
        move(self, direction): Get the next room from the exits dictionary of the current room and set the current room to the next room.

    """
    
    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.Historique = []
        self.liste_directions = {"O" : ["O", "o", "Ouest", "OUEST", "ouest"], 
                                 "E" : ["E", "e", "Est", "EST", "est"], 
                                 "S" : ["S", "s", "Sud", "SUD", "sud"], 
                                 "N" : ["N", "n", "Nord", "NORD", "nord"], 
                                 "U" : ["U", "u", "Up", "UP", "up"], 
                                 "D" : ["D", "d", "Down", "DOWN", "down"],
                                 "SO" : ["SO", "so", "Sud-Ouest", "SUD-OUEST", "sud-ouest"],
                                 "SE" : ["SE", "se", "Sud-Est", "SUD-EST", "sud-est"],
                                 "NO" : ["NO", "no", "Nord-Ouest", "NORD-OUEST", "nord-ouest"],
                                 "NE" : ["NE", "ne", "Nord-Est", "NORD-EST", "nord-est"]}
        self.inventory = {}
        self.max_weight = None
        self.current_weight = 0

    # Define the move method.
    def move(self, direction):
        for i in self.liste_directions.keys():
            if direction in self.liste_directions[i]:
                direction = i
                break

        # Get the next room from the exits dictionary of the current room.
        try:
            next_room = self.current_room.exits[direction]
        except KeyError:
            next_room = None

        if self.current_room.name == "Entrée Nord" and direction in ["NO", "N", "NE"]:
            print("\nQue faites-vous ? Vous avez des gens à sauver et ils ne sont pas dans cette direction !\n")
            return False
        if self.current_room.name == "Entrée Ouest" and direction in ["NO", "O", "SO", "S"]:
            print("\nQue faites-vous ? Vous avez des gens à sauver et ils ne sont pas dans cette direction !\n")
            return False
        if self.current_room.name == "Entrée Est" and direction in ["NE", "E", "SE", "S"]:
            print("\nQue faites-vous ? Vous avez des gens à sauver et ils ne sont pas dans cette direction !\n")
            return False

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.history.append(self.current_room)
        if self.current_room not in self.Historique:
            self.Historique.append(self.current_room)
        self.current_room = next_room
        print(self.current_room.get_long_description())
    #    self.get_history()
    #    self.get_Historique()
        return True

    def get_history(self):
        if self.history == []:
            print("\nVous n'avez pas d'historique pour l'instant\n")
            return False
        else:
            print("\nVous avez déja visité les pièces suivantes:")
            for i in self.history:
                print(f"\t- {i.name}")
            print("")
            return True
        
    def get_Historique(self):
        if self.Historique == []:
            print("\nVous n'avez pas d'historique pour l'instant\n")
            return False
        else:
            print("\nVous avez déja visité au moins une fois les pièces suivantes:")
            for i in self.Historique:
                print(f"\t- {i.name}")
            print("")
            return True
    
    def move_back(self):
        if self.history == []:
            print("\nVous n'avez pas de lieux accessibles avec cette commande\n")
            return False
        
        for i in self.current_room.exits.keys():
            if self.current_room.exits[i] == self.history[-1]:
                self.current_room = self.history.pop()
                print(self.current_room.get_long_description())
                return True

        print("\nLa zone précédente n'est pas accessible par retour en arrière (sens unique notamment).\nL'historique sera effacé par conséquent.")
        print("Il est cependant possible d'accéder à la liste des lieux déjà visités durant toute la partie avec la commande 'Historique'.\n")
        self.history = []
        return False
    
    def get_inventory(self):
        if self.inventory == {}:
            print("\nVotre inventaire est vide.\n")
            print(f"Espace de stockage disponible : {self.max_weight - self.current_weight} kg\n")
            return False
        else:
            print("\nVous disposez des items suivants :")
            for item in self.inventory.keys():
                print("\t- " + str(self.inventory[item]))
            print(f"\nEspace de stockage disponible : {self.max_weight - self.current_weight} kg\n")
            return True