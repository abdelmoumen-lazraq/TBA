# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
from quest import Quest


DEBUG = True

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.character = {}
        

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
        talk = Command("talk", " : permet d'engager la discussion avec le PNJ sélectionné en paramètre", Actions.talk, 1)
        self.commands["talk"] = talk
        quests = Command("quests", " : afficher la liste des quêtes", Actions.quests, 0)
        self.commands["quests"] = quests

        quest = Command("quest", " <titre> : afficher les détails d'une quête", Actions.quest, 1)
        self.commands["quest"] = quest

        activate = Command("activate", " <titre> : activer une quête", Actions.activate, 1)
        self.commands["activate"] = activate

        rewards = Command("rewards", " : afficher vos récompenses", Actions.rewards, 0)
        self.commands["rewards"] = rewards
        # Setup rooms

        entree_nord = Room("Entrée Nord","à l’entrée principale de l’ESIEE (entrée nord), devant l'axe de la terre, où convergent étudiants et visiteurs.")
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

        # Setup items

        papier_dechire = Item("papier déchiré", "petit papier où il semble y avoir quelque chose d'écrit...", 0.003)
        entree_nord.inventory["papier déchiré"] = papier_dechire

        # Setup characters

        cody = Character("Cody", "un petit robot semblant fonctionner par IA", entree_nord)
        cody.msgs["Premier message"] = "Bip Bip Bonjour, je suis Cody, je suis une intelligence artificielle" \
        "\nJ'aurais besoin de ton aide pour régler cette énorme panne avant que ça n'empire et que ça devienne dangereux pour les personnes bloquées à l'intérieur Bip Bip."
        cody.msgs["Présentation"] = "Bip Bip Bonjour, je suis Cody, je suis une intelligence artificielle"
        cody.msgs["Requête"] = "J'aurais besoin de ton aide pour régler cette énorme panne avant que ça n'empire et que ça devienne dangereux pour les personnes bloquées à l'intérieur Bip Bip."
        entree_nord.character["Cody"] = cody
        self.character["Cody"] = cody

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = entree_nord
        self.player.max_weight = 20

        self._setup_quests()  

    def _setup_quests(self):
        """Initialize all quests."""
        exploration_quest = Quest(
            title="Explorateur de l'ESIEE",
            description="Explorez les lieux principaux de l'école.",
            objectives=["Visiter Entrée Nord",
                        "Visiter Hall d'accueil",
                        "Visiter Bibliothèque"],
            reward="Badge Explorateur"
        )

        interaction_quest = Quest(
            title="Parler à Cody",
            description="Engager la discussion avec Cody.",
            objectives=["parler avec Cody"],
            reward="Information secrète"
        )

        item_quest = Quest(
            title="Message mystérieux",
            description="Récupérer le papier déchiré.",
            objectives=["prendre papier déchiré"],
            reward="Indice important"
        )

        self.player.quest_manager.add_quest(exploration_quest)
        self.player.quest_manager.add_quest(interaction_quest)
        self.player.quest_manager.add_quest(item_quest)
    # Play the game
    def play(self):
        """Main game loop."""

        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
            if self.loose():
                print("\n💀 Vous avez perdu la partie. Essayez de nouveau !\n")
                self.finished = True

            elif self.win():
                print("\nFélicitations ! Vous avez accompli toutes les quêtes du jeu et sauvé l'école !\n")
                self.finished = True
    def win(self):
        """Return True if all quests are completed."""
        return self.player.quest_manager.all_quests_completed()
    
    def loose(self):
        """Return True if defeat conditions are met."""
        if self.player.current_room.name == "Salle blanche":
            if "papier déchiré" not in self.player.inventory:
                print("\n💀 Vous êtes entré dans la salle blanche sans l’indice nécessaire.")
                return True
        return False



    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        """Process the command entered by the player."""

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands:
            msg1 = f"\nCommande '{command_word}' non reconnue."
            msg2 = " Entrez 'help' pour voir la liste des commandes disponibles.\n"
            print(msg1 + msg2)
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)


    # Print the welcome message
    def print_welcome(self):
        """Print the welcome message."""

        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")

        print(self.player.current_room.get_long_description())
    

def main():
    """Create a game object and play the game"""
    Game().play()


if __name__ == "__main__":
    main()
