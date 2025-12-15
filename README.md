SIEE LOCKDOWN
Quatre chiffres, un code, une école à sauver

Présentation du jeu
Une panne d’électricité générale a frappé l’ESIEE Paris.
Toutes les portes se verrouillent automatiquement et les systèmes de sécurité empêchent toute sortie.

Les étudiants et les professeurs se retrouvent piégés dans les salles.
Vous êtes le seul encore en mesure de vous déplacer librement dans l’établissement.

Votre mission :
Explorer les bâtiments de l’ESIEE, résoudre des énigmes et réunir les quatre chiffres nécessaires pour former le code de sécurité permettant de réactiver le système et libérer tout le monde.

Ce jeu est une aventure textuelle interactive, jouable entièrement dans la console Python.

Commandes du jeu
help : Affiche toutes les commandes disponibles
go <direction> : Permet de se déplacer (N, S, E, O, U, D, etc.)
history : Affiche l’historique complet des déplacements
back : Retour à la salle précédente
quit : Quitter le jeu

L’univers du jeu
L’aventure se déroule au sein de plusieurs lieux emblématiques de l’ESIEE :
- Entrée Nord (lieu de départ)
- Entrée Est et Entrée Ouest
- Hall d’accueil
- Zone intérieure Est et Zone intérieure Ouest
- Bibliothèque
- Salle blanche
- Bâtiments EPI1 à EPI6 (3 étages chacun)

Chaque salle possède une description immersive.
Certaines contiennent des indices ou des énigmes permettant de trouver l’un des chiffres du code.

Objectif principal : Trouver le  Code de déverrouillage
Pour sauver l’ESIEE vous devez :
- Trouver les quatre chiffres disséminés dans l’école
- Former le code de déverrouillage

Sans ce code, les portes resteront fermées.
Avec ce code, l’ESIEE est sauvée.

Architecture du projet:

Le jeu est développé selon une architecture orientée objet :
- Game : Gestion de la boucle principale et des commandes
- Room : Représentation des salles et de leurs sorties
- Player : Gestion de la position et de l’historique
- Command : Structure de chaque commande
- Actions : Exécution des différentes actions
- Items : Gestion des objets                       #Coming
- Character : Gestion des personnages non joueurs  #Coming

Lancement du jeu :

Lancer le fichier game.py depuis un terminal.
Entrer son nom pour commencer l’aventure.

Améliorations possibles:

- Enigmes et objectifs secondaires
- Interface graphique 
- Dialogues évolués avec les PNJ


Plan de développement du projet
1) Introduction : 20 novembre
2) Une Première version  : 20 novembre
3) Votre propre univers (ajout des lieux ESIEE) : 22 novembre
4) Ajout de l’historique (history + back) : 30 novembre
5) Ajout des objets et inventaire : Coming soon
6) Ajout des PNJ : Coming
7) Ajout des quêtes  : Coming
8) Ajout une interface graphique : Coming