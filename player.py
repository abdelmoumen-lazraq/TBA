"""Define the Player class."""

from room import Room
from quest import QuestManager

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
        self.move_count = 0
        self.quest_manager = QuestManager(self)
        self.rewards = []  # List to store earned rewards
        self.game = None

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

        # Petit bonus lorsque le joueur essaie de quitter la zone jouable
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
        
        # Remplie les deux historiques des zones visitées
        self.history.append(self.current_room)
        if self.current_room not in self.Historique:
            self.Historique.append(self.current_room)

        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        if next_room.name == "Salle blanche":
            print("\n   GAME OVER")
            print("\nVous avez été électrocuté en rentrant dans la Salle Blanche")
            print("L'instabilité du courant n'a pas été réglée et vous a couté la vie\n")
            self.game.finished = True
            return False



        # Check room visit objectives
        self.quest_manager.check_room_objectives(self.current_room.name)

        # Increment move counter and check movement objectives
        self.move_count += 1
        self.quest_manager.check_counter_objectives("Se déplacer", self.move_count)

        return True
    
    def ramasse_papier(self, objet):
        self.quest_manager.check_action_objectives("Ramasser", objet)
        return None


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



    def add_reward(self, reward):
        """
        Add a reward to the player's rewards list.
        
        Args:
            reward (str): The reward to add.
            
        Examples:
        
        >>> player = Player("Bob")
        >>> player.add_reward("Épée magique") # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Vous avez obtenu: Épée magique
        <BLANKLINE>
        >>> "Épée magique" in player.rewards
        True
        >>> player.add_reward("Épée magique") # Adding same reward again
        >>> len(player.rewards)
        1
        """
        if reward and reward not in self.rewards:
            self.rewards.append(reward)
            print(f"\n🎁 Vous avez obtenu: {reward}\n")


    def show_rewards(self):
        """
        Display all rewards earned by the player.
        
        Examples:
        
        >>> player = Player("Charlie")
        >>> player.show_rewards() # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Aucune récompense obtenue pour le moment.
        <BLANKLINE>
        >>> player.add_reward("Bouclier d'or") # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Vous avez obtenu: Bouclier d'or
        <BLANKLINE>
        >>> player.show_rewards() # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Vos récompenses:
        • Bouclier d'or
        <BLANKLINE>
        """
        if not self.rewards:
            print("\n🎁 Aucune récompense obtenue pour le moment.\n")
        else:
            print("\n🎁 Vos récompenses:")
            for reward in self.rewards:
                print(f"  • {reward}")
            print()