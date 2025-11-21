# Define the Player class.
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
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits.get(direction)

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    