# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.valid_directions = set()
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, U, D)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms
        entree_nord = Room("Entrée Nord","L’entrée principale de l’ESIEE, devant l'axe de la terre,  où convergent étudiants et visiteurs.")
        self.rooms.append(entree_nord)

        entree_est = Room("Entrée Est","L’entrée est, située juste à côté du RU CROUS, toujours animée aux heures de repas.")   
        self.rooms.append(entree_est)

        entree_ouest = Room("Entrée Ouest", "L’entrée ouest, l’accès quotidien des étudiants près du parking et du RER.")
        self.rooms.append(entree_ouest)

        hall = Room("Hall d'accueil", "le hall d’accueil, un vaste espace lumineux rempli de panneaux d’information.")
        self.rooms.append(hall)

        zone_interieure_est = Room("Zone intérieure Est", "la zone intérieure Est, juste en face de l’amphi Marcel Dassault.")
        self.rooms.append(zone_interieure_est)

        zone_interieure_ouest = Room("Zone intérieure Ouest", "la zone intérieure Ouest, située en face des bureaux administratifs.")
        self.rooms.append(zone_interieure_ouest)

        bibliotheque = Room("Bibliothèque", "la bibliothèque, entourée de rayonnages remplis de livres et d’espaces de travail calmes.")
        self.rooms.append(bibliotheque)

        salle_blanche = Room("Salle blanche", "la salle blanche, remplie d’équipements techniques sensibles et d’appareils spécialisés.")
        self.rooms.append(salle_blanche)

        epi1 = Room("EPI1", "l’EPI1, où les écrans affichent des lignes de code et des logiciels en plein développement.")
        self.rooms.append(epi1)

        epi2 = Room("EPI2", "l’EPI2, où traînent des cartes électroniques et des prototypes en cours d’expérimentation.")
        self.rooms.append(epi2)

        epi3 = Room("EPI3", "l’EPI3, un laboratoire où l’on entend le bruit constant des ventilateurs des ordinateurs.")
        self.rooms.append(epi3)

        epi4 = Room("EPI4", "l’EPI4, un espace où les étudiants travaillent sur des projets variés et innovants.")
        self.rooms.append(epi4)

        epi5 = Room("EPI5", "l’EPI5, rempli de maquettes, de prototypes et d’outils éparpillés partout.")
        self.rooms.append(epi5)

        epi6 = Room("EPI6", "l’EPI6, un laboratoire doté d’une grande baie vitrée donnant sur l’extérieur.")
        self.rooms.append(epi6)

        # Create exits for rooms

        # Rez-de-chaussée
        entree_nord.exits = {"S": hall, "O": bibliotheque,}

        entree_est.exits = {"O": zone_interieure_est}

        entree_ouest.exits = {"E": zone_interieure_ouest}

        hall.exits = {"N": entree_nord, "E": zone_interieure_est, "O": zone_interieure_ouest}

        zone_interieure_est.exits = {"E": entree_est, "S": salle_blanche, "O": hall, "U": epi4, "D": epi5} 

        zone_interieure_ouest.exits = {"N": bibliotheque , "E": hall, "S": epi1, "O": entree_ouest, "U": epi2, "D": epi3}

        bibliotheque.exits = {"E": entree_nord, "S": zone_interieure_ouest}

        salle_blanche.exits = {"N": zone_interieure_est, "D": epi6}

        # Étage (EPI)
        epi1.exits = {"N": zone_interieure_ouest, "E": epi2,}  

        epi2.exits = {"O": epi1, "U": epi3, "D": zone_interieure_ouest}

        epi3.exits = {"U": zone_interieure_ouest, "D": epi2}

        epi4.exits = {"U": epi5, "D": zone_interieure_ouest}

        epi5.exits = {"E": epi6, "U": zone_interieure_est, "D": epi4}

        epi6.exits = {"O": epi5, "U": salle_blanche}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = entree_nord
        self.valid_directions = set()
        for room in self.rooms:
            self.valid_directions.update(room.exits.keys())

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            if command_word != "":
                print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
