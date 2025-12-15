# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction, que ce soit dans une des directions cardinales ou bien monter/déscendre ou alors une direction bien précise", Actions.go, 1)
        self.commands["go"] = go
        history = Command("history", " : affiche l'historique des endroits visités dans l'ordre de visite (peut inclure des répétitions)", Actions.history, 0)
        self.commands["history"] = history
        Historique = Command("Historique", " : affiche l'historique de tous les endroits visités durant la partie sans doublons (historique non effaçable)", Actions.Historique, 0)
        self.commands["Historique"] = Historique
        back = Command("back", " : retour à l'endroit précédemment visité (si possible)", Actions.back, 0)
        self.commands["back"] = back
        check = Command("check", " : affiche l'inventaire des objets que vous avez ainsi que l'espace libre", Actions.check, 0)
        self.commands["check"] = check
        look = Command("look", " : affiche les objets présents dans la zone où vous vous trouvez", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " : ramasse l'objet désigné, remplissant l'inventaire du joueur", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " : sélectionne l'objet depuis l'inventaire et le dépose dans la zone actuelle", Actions.drop, 1)
        self.commands["drop"] = drop
        
        # Setup rooms

        entree_nord = Room("Entrée Nord","à l’entrée principale de l’ESIEE, devant l'axe de la terre, où convergent étudiants et visiteurs.")
        self.rooms.append(entree_nord)
        entree_est = Room("Entrée Est","à l’entrée est, située juste à côté du RU CROUS, toujours animée aux heures de repas.")   
        self.rooms.append(entree_est)
        entree_ouest = Room("Entrée Ouest", "à l’entrée ouest, l’accès quotidien des étudiants près du parking et du RER.")
        self.rooms.append(entree_ouest)
        hall = Room("Hall d'accueil", "dans le hall d’accueil, un vaste espace lumineux rempli de panneaux d’information.")
        self.rooms.append(hall)
        zone_interieure_est = Room("Zone intérieure Est", "dans la zone intérieure Est, juste en face de l’amphi Marcel Dassault.")
        self.rooms.append(zone_interieure_est)
        zone_interieure_ouest = Room("Zone intérieure Ouest", "dans la zone intérieure Ouest, située en face des bureaux administratifs.")
        self.rooms.append(zone_interieure_ouest)
        bibliotheque = Room("Bibliothèque", "dans la bibliothèque, entourée de rayonnages remplis de livres et d’espaces de travail calmes.")
        self.rooms.append(bibliotheque)
        salle_blanche = Room("Salle blanche", "dans la salle blanche, remplie d’équipements techniques sensibles et d’appareils spécialisés.")
        self.rooms.append(salle_blanche)

        epie1 = Room("Epie1", "dans l’EPI1, où les écrans affichent des lignes de code et des logiciels en plein développement.")
        self.rooms.append(epie1)
        epie1_etage1 = Room("Epie 1 étage 1", "à l'étage 1 de l'épie 1.")
        self.rooms.append(epie1_etage1)
        epie1_etage2 = Room("Epie 1 étage 2", "à l'étage 2 de l'épie 1.")
        self.rooms.append(epie1_etage2)
        epie1_etage3 = Room("Epie 1 étage 3", "à l'étage 3 de l'épie 1.")
        self.rooms.append(epie1_etage3)

        epie2 = Room("Epie2", "dans l’EPI2, où traînent des cartes électroniques et des prototypes en cours d’expérimentation.")
        self.rooms.append(epie2)
        epie2_etage1 = Room("Epie 2 étage 1", "à l'étage 1 de l'épie 2.")
        self.rooms.append(epie2_etage1)
        epie2_etage2 = Room("Epie 2 étage 2", "à l'étage 2 de l'épie 2.")
        self.rooms.append(epie2_etage2)
        epie2_etage3 = Room("Epie 2 étage 3", "à l'étage 3 de l'épie 2.")
        self.rooms.append(epie2_etage3)

        epie3 = Room("Epie3", "dans l’EPI3, un laboratoire où l’on entend le bruit constant des ventilateurs des ordinateurs.")
        self.rooms.append(epie3)
        epie3_etage1 = Room("Epie 3 étage 1", "à l'étage 1 de l'épie 3.")
        self.rooms.append(epie3_etage1)
        epie3_etage2 = Room("Epie 3 étage 2", "à l'étage 2 de l'épie 3.")
        self.rooms.append(epie3_etage2)
        epie3_etage3 = Room("Epie 3 étage 3", "à l'étage 3 de l'épie 3.")
        self.rooms.append(epie3_etage3)

        epie4 = Room("Epie4", "dans l’EPI4, un espace où les étudiants travaillent sur des projets variés et innovants.")
        self.rooms.append(epie4)
        epie4_etage1 = Room("Epie 4 étage 1", "à l'étage 1 de l'épie 4.")
        self.rooms.append(epie4_etage1)
        epie4_etage2 = Room("Epie 4 étage 2", "à l'étage 2 de l'épie 4.")
        self.rooms.append(epie4_etage2)
        epie4_etage3 = Room("Epie 4 étage 3", "à l'étage 3 de l'épie 4.")
        self.rooms.append(epie4_etage3)
        
        epie5 = Room("Epie5", "dans l’EPI5, rempli de maquettes, de prototypes et d’outils éparpillés partout.")
        self.rooms.append(epie5)
        epie5_etage1 = Room("Epie 5 étage 1", "à l'étage 1 de l'épie 5.")
        self.rooms.append(epie5_etage1)
        epie5_etage2 = Room("Epie 5 étage 2", "à l'étage 2 de l'épie 5.")
        self.rooms.append(epie5_etage2)
        epie5_etage3 = Room("Epie 5 étage 3", "à l'étage 3 de l'épie 5.")
        self.rooms.append(epie5_etage3)
        
        epie6 = Room("Epie6", "dans l’EPI6, un laboratoire doté d’une grande baie vitrée donnant sur l’extérieur.")
        self.rooms.append(epie6)
        epie6_etage1 = Room("Epie 6 étage 1", "à l'étage 1 de l'épie 6.")
        self.rooms.append(epie6_etage1)
        epie6_etage2 = Room("Epie 6 étage 2", "à l'étage 2 de l'épie 6.")
        self.rooms.append(epie6_etage2)
        epie6_etage3 = Room("Epie 6 étage 3", "à l'étage 3 de l'épie 6.")
        self.rooms.append(epie6_etage3)

        # Create exits for rooms

        entree_nord.exits = {"O" : entree_ouest, "E" : entree_est, "S" : hall}
        entree_est.exits = {"O" : zone_interieure_est, "N" : entree_nord}
        entree_ouest.exits = {"E" : zone_interieure_ouest, "N" : entree_nord}
        hall.exits = {"N" : entree_nord, "O" : zone_interieure_ouest, "E" : zone_interieure_est}
        zone_interieure_est.exits = {"O" : hall, "E" : entree_est, "SO" : epie4, "S" : epie5, "SE" : epie6}
        zone_interieure_ouest.exits = {"E" : hall, "O" : entree_ouest, "N" : bibliotheque, "SO" : epie1, "S" : epie2, "SE" : epie3}
        bibliotheque.exits = {"S" : zone_interieure_ouest}
        salle_blanche.exits = {"O" : epie6}

        epie1.exits = {"N" : zone_interieure_ouest, "U" : epie1_etage1}
        epie1_etage1.exits = {"U" : epie1_etage2, "D" : epie1}
        epie1_etage2.exits = {"U" : epie1_etage3, "D" : epie1_etage1}
        epie1_etage3.exits = {"E" : epie1, "D" : epie1_etage2}
        
        epie2.exits = {"N" : zone_interieure_ouest, "U" : epie2_etage1}
        epie2_etage1.exits = {"U" : epie2_etage2, "D" : epie2}
        epie2_etage2.exits = {"U" : epie2_etage3, "D" : epie2_etage1}
        epie2_etage3.exits = {"E" : epie2, "D" : epie2_etage2}

        epie3.exits = {"N" : zone_interieure_ouest, "U" : epie3_etage1}
        epie3_etage1.exits = {"U" : epie3_etage2, "D" : epie3}
        epie3_etage2.exits = {"U" : epie3_etage3, "D" : epie3_etage1}
        epie3_etage3.exits = {"E" : epie3, "D" : epie3_etage2}

        epie4.exits = {"N" : zone_interieure_est, "U" : epie4_etage1}
        epie4_etage1.exits = {"U" : epie4_etage2, "D" : epie4}
        epie4_etage2.exits = {"U" : epie4_etage3, "D" : epie4_etage1}
        epie4_etage3.exits = {"E" : epie4, "D" : epie4_etage2}
        
        epie5.exits = {"N" : zone_interieure_est, "U" : epie5_etage1}
        epie5_etage1.exits = {"U" : epie5_etage2, "D" : epie5}
        epie5_etage2.exits = {"U" : epie5_etage3, "D" : epie5_etage1}
        epie5_etage3.exits = {"E" : epie5, "D" : epie5_etage2}
        
        epie6.exits = {"N" : zone_interieure_est, "E" : salle_blanche, "U" : epie6_etage1}
        epie6_etage1.exits = {"U" : epie6_etage2, "D" : epie6}
        epie6_etage2.exits = {"U" : epie6_etage3, "D" : epie6_etage1}
        epie6_etage3.exits = {"E" : epie6, "D" : epie6_etage2}

        # Setup player and starting room

        papier_dechire = Item("papier déchiré", "petit papier où il semble y avoir quelque chose d'écrit...", 0.003)
        entree_nord.inventory["papier déchiré"] = papier_dechire

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = entree_nord
        self.player.max_weight = 20

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
