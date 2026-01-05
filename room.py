# Define the Room class.

class Room:
    """
    This class represents a room. A room is composed of a name, a description and some exits.

    Attributes:
        name (str): The name of the room.
        description (str): Its description.
        exits (dict): The exits directions as keys and the nexts rooms linked as values.

    Methods:
        __init__(self, name, description) : The constructor.
        get_exit(self, direction) : Return the room in the given direction if it exists.
        get_exit_string(self) : Return a string describing the room's exits.
        get_long_description(self): Return a long description of this room including exits.

    """

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
        self.characters = []
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties:" 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += "\n\t- " + exit + f" : {self.exits[exit].name}"
        # exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"

    # Display the content of the room (items + PNJ)
    def get_inventory(self):
        # La salle est vide uniquement si elle ne contient ni objets ni PNJ
        if not self.inventory and not self.characters:
            print("\nIl n'y a rien ici.\n")
            return False

        print("\nOn voit:")

        # Affichage des objets
        for item in self.inventory.values():
            print("\t- " + str(item))

        # Affichage des personnages non joueurs
        for character in self.characters:
            print("\t- " + str(character))

        print()
        return True
