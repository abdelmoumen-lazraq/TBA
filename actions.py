# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        PNJ_cody = game.character["Cody"]
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction = list_of_words[1]

        # On s'assure d'abord que la direction choisie est correct.
        n = 0
        m = 0
        for i in player.liste_directions.keys():
            m += 1
            if direction not in player.liste_directions[i]:
                n += 1

        if m == n:
            print(f"\nDirection '{direction}' non reconnue.\n")
            return False

        # Move the player in the direction specified by the parameter.
        player.move(direction)
        PNJ_cody.move()
        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    def history(game, list_of_words, number_of_parameters):

        # If the number of parameters is incorrect, print an error message and return False.
        player = game.player
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player.get_history()
        return True
    
    def Historique(game, list_of_words, number_of_parameters):

        # If the number of parameters is incorrect, print an error message and return False.
        player = game.player
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player.get_Historique()
        return True
    
    def back(game, list_of_words, number_of_parameters):

        # If the number of parameters is incorrect, print an error message and return False.
        player = game.player
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player.move_back()
        return True
    
    def check(game, list_of_words, number_of_parameters):

        # If the number of parameters is incorrect, print an error message and return False.
        player = game.player
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player.get_inventory()
        return True
    
    def look(game, list_of_words, number_of_parameters):

        # If the number of parameters is incorrect, print an error message and return False.
        current_room = game.player.current_room
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        print(current_room.get_long_description())
        current_room.get_inventory()
        current_room.get_character()
        return True
    
    def take(game, list_of_words, number_of_parameters):

        # If the number of parameters is incorrect, print an error message and return False.
        current_room = game.player.current_room
        player = game.player
        l = len(list_of_words)
        objet_str = ""
        
        if l <= number_of_parameters :
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        for i in range(1, l):
            objet_str += list_of_words[i] + " "
        objet_str = objet_str.rstrip()
        objet = current_room.inventory[objet_str]
        
        if objet_str in current_room.inventory.keys() and objet.weight <= player.max_weight - player.current_weight:
            player.inventory[objet_str] = current_room.inventory[objet_str]
            del current_room.inventory[objet_str]
            print(f"\nL'objet '{objet_str}' a été ramassé.\n")
            player.current_weight = player.current_weight + objet.weight
            return True
        elif objet.weight > player.max_weight - player.current_weight:
            print(f"\nL'objet '{objet_str}' surcharge l'inventaire. Vous ne pouvez actuellement pas le prendre.\n")
            return False
        else:
            print("\nIl n'existe pas un tel objet dans cette zone.\n")
            return False
    
    def drop(game, list_of_words, number_of_parameters):

        # If the number of parameters is incorrect, print an error message and return False.
        current_room = game.player.current_room
        player = game.player
        l = len(list_of_words)
        objet_str = ""

        if l <= number_of_parameters :
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        for i in range(1, l):
            objet_str += list_of_words[i] + " "
        objet_str = objet_str.rstrip()
        objet = player.inventory[objet_str]
        
        if objet_str in player.inventory.keys():
            current_room.inventory[objet_str] = player.inventory[objet_str]
            del player.inventory[objet_str]
            print(f"\nL'objet '{objet_str}' a été déposé dans cette zone.\n")
            player.current_weight = player.current_weight - objet.weight
            return True
        else:
            print("\nVous ne possédez pas un tel objet dans votre inventaire.\n")
            return False
    
    def talk(game, list_of_words, number_of_parameters):
        player = game.player
        current_room = player.current_room
        l = len(list_of_words)
        PNJ_str = ""

        if l <= number_of_parameters :
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        for i in range(1, l):
            PNJ_str += list_of_words[i] + " "
        PNJ_str = PNJ_str.rstrip()

        if PNJ_str not in current_room.character.keys():
            print(f"\nCe PNJ n'est pas dans la pièce.\n")
            return False
        else:
            PNJ = current_room.character[PNJ_str]
            PNJ.talk()
            return True