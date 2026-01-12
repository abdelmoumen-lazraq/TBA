from room import Room
import random as random


class Character:

    def __init__(self, name, description, current_room):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = {}
        self.proba_déplacement = None
        self.player = None
    
    def __str__(self):
        return  self.name \
                + " : " \
                + self.description
    
    def move(self):
        from game import DEBUG
        if random.choice(self.proba_déplacement) > 1:
        # if self.proba_déplacement > 1:
            if DEBUG:
                print(f"\nDEBUG : {self.name} n'a pas bougé et se trouve dans la zone '{self.current_room.name}'\n")
            return False

        else:
            liste_sorties = []
            for i in self.current_room.exits.keys():
                liste_sorties.append(self.current_room.exits[i])

            next_room = random.choice(liste_sorties)
            next_room.character[self.name] = self.current_room.character.pop(self.name)
            self.current_room = next_room
            if DEBUG:
                print(f"DEBUG : {self.name} s'est déplacé dans la zone '{self.current_room.name}'\n")
            return True
    
    def talk(self):
        discussion = True
        m = 0
        if "Premier message" in self.msgs.keys():
            print(f"\n{self.name} : {self.msgs.pop("Premier message")}\n")
            m = 1
        if m == 0:
            print(f"\n{self.name} : {self.msgs["Présentation"]}\n")
        
        m = 0
        dic = {}
        if self.msgs != {}:
            for i in self.msgs.keys():
                m += 1
                print(f"\t- {i} ({m})")
                dic[m] = i
            print("\t- Quitter la conversation (0)")
        if self.msgs == {}:
            discussion = False
            return False
        
        while discussion:
            e = input("\n>>> Choisissez ce dont vous voulez parler : ")
            print("")
            
            try:
                if e == "0":
                    discussion = False
                elif int(e) <= m :
                    print(f"{self.msgs[dic[int(e)]]}\n")
                    key = dic[int(e)]
                    list_of_words = key.split(" ")
                    if list_of_words[0] == "Quête":
                        self.check_quest_talk_choice("Parler", self.name)
                        discussion = False
                        del self.msgs[key]
                else:
                    print(f"**Attention** : le choix doit être compris entre 0 et {m}")
            except ValueError:
                print(f"**Attention** : '{e}' n'est pas un choix valide")


    def add_quest_Cody(self, quest_number):
        if self.name != "Cody":
            return False
        else:
            quest_dic = {}
            quest_dic[1] = "Oh, tu m'as ramené des choses à déchiffrer ? Fais-moi voir ça."
            
            self.msgs[f"Quête {quest_number}"] = quest_dic[quest_number]
    
    def check_quest_talk_choice(self, action, target):
        # from quest import QuestManager
        self.player.quest_manager.check_action_objectives(action, target)
        return True