from Part2 import *
import platform
from os import system, path
import json

def creer_partie(n):
	"""
	Crée une partie. Une partie est un dictionnaire contenant :
	- le joueur dont c'est le tour (clé joueur) initialisé à 1,
	- le plateau (clé plateau).
	"""
	return {"joueur":1, "plateau": creer_plateau(n)} #Retourne une partie créée 

def saisie_valide(partie, s):
	"""
	Retourne True si la chaîne s correspond à un mouvement valide pour le joueur
	et False sinon.
	La chaîne s est valide si :
	- s est égal à la lettre M ou
	- s correspond à une case (de la forme a1 pour la case (0,0), ..., h8 pour la cas
	où le joueur courant peut poser son pion.
	"""
	if s == "M": #Si l'utilisateur choisi "M" pour accerder au menu
		return True
	if len(s) == 2: #Vérifie que la taille de la chaine de charactère vaut maximum 2 
		i = ord(s[0])-97 #Permet de récupérer la ligne 
		j = int(s[1])-1 #Permet de récupérer la colone 
		case = case_valide(partie["plateau"],i,j) #Vérifie que la case est valide
		mouvement = mouvement_valide(partie["plateau"], i, j, partie["joueur"]) #Vérifie que le mouvement est valide
		vide = get_case(partie["plateau"], i,j) == 0 #Récupère la valeur de la case
		if vide and mouvement and case: #Vérifie que la case et le mouvement est valide ainsi que la valeur de la case 
			return True
		else:
			return False
	else:
		return False

def efface_term():
	if platform.system() == 'Linux': #Vérifie que l'ordinateur fonctionne sous Linux
		system("clear") #Efface le terminal
	elif platform.system() == 'Windows': #Vérifie que l'ordinateur fonctionne sous Windows
		system("cls") #Efface le terminal

def tour_jeu(partie):
	"""
	Effectue un tour de jeu :
	- efface le terminal,
	- affiche le plateau,
	- si le joueur courant peut jouer, effectue la saisie d'un mouvement valide
	(saisie contrôlée),
	- Effectue le mouvement sur le plateau de jeu,
	- Retourne True si le joueur courant a joué ou False s'il souhaite accéder
	au menu principal."""
	
	efface_term() #Efface le terminal 
	afficher_plateau_colore(partie["plateau"]) #Affiche le plateau en couleur 
	if joueur_peut_jouer(partie["plateau"], partie["joueur"]):
		if partie["joueur"] == 1: #
			j = "noir"            #Permet de déterminer le joueur et la couleur de son pion
		else:                     #
			j = "blanc"           #
		s = ''
		while saisie_valide(partie, s) == False:
			s = input("Joueur "+j+" choisissez une case: ") #Permet de choisir une case
		if s == "M": #Si l'utilisateur choisi le menu alors retourne False
			return False
		else:
			mouvement(partie["plateau"], ord(s[0])-97, int(s[1])-1, partie["joueur"]) #Effectue le mouvement
			return True

def interprete_action(n, partie):
	if n == 0:
		print("Fin de partie.")
		print("Au revoir..")
		exit() #Si la valeur entrée est 0, alors l'utilisateur est sorti du terminal
	if n == 1:
		t = saisir_taille_plateau()
		partie = creer_partie(t)
		jouer(partie) #Si la valeur entrée est 1, alors l'utilisateur joue une nouvelle partie
	if n == 2:
		if path.exists("sauvegarde_partie.json"): #Si la sauvegarde existe
			file = open("sauvegarde_partie.json", "r") #On ouvre le fichier 
			partie = json.load(file) #On charge le fichier
			jouer(partie) #Si la valeur entrée est 0, alors l'utilisateur est sorti du terminal
		else:
			print("Le fichier sauvegarde_partie.json n'existe pas.")
	if n == 3:
		if partie is None:
			print('Aucune partie à sauvegardée')
		else:
			file = open("sauvegarde_partie.json", "w") #On ouvre un fichier
			json.dump(partie, file) #On sauvegarde la partie dans le fichier
			print("\nPartie sauvegardée")
	if n == 4:
		if partie is None:
			print("Aucune partie en cours.")
		else:
			print()
			jouer(partie) #Si la valeur entrée est 4, alors l'utilisateur peut rependre une partie

def saisir_action(partie):
	"""
	Retourne le choix du joueur pour menu (saisie contrôlée):
	- 0 pour terminer le jeu,
	- 1 pour commencer une nouvelle partie,
	- 2 pour charger une partie,
	- 3 pour sauvegarder une partie (si une partie est en cours),
	- 4 pour reprendre la partie (si une partie est en cours).
	"""
	print()
	print("[+] MENU [+]")
	print(" - 0 pour terminer le jeu")
	print(" - 1 pour commencer une nouvelle partie")
	print(" - 2 pour charger une partie")
	print(" - 3 pour sauvegarder une partie (si une partie est en cours)")
	print(" - 4 pour reprendre la partie (si une partie est en cours)")
	n = -1
	while n < 0 or n > 4: #Vérifie que le choix est bien un chiffre compris entre 0 et 1
		n = int(input('Entrez votre choix: ')) #Permet de rentrer un entier 
	return n

def jouer(partie) :
	"""
	Permet de jouer à la partie en cours (passée en paramètre).
	Retourne True si la partie est terminée, False sinon."""
	while fin_de_partie(partie["plateau"]) == False: 
		if tour_jeu(partie) == False:
			action = saisir_action(partie)  #Renvoie vers le menu si aucun joueur ne joue
			interprete_action(action, partie)
		else:
			if partie["joueur"] == 1: #Alterne les joueurs
				partie["joueur"] = 2  #
			else:                     
				partie["joueur"] = 1  

	efface_term() #Efface le terminal
	print("\nPartie terminée.")
	afficher_plateau_colore(partie['plateau']) #Affiche le plateau en couleur
	if gagnant(partie["plateau"]) == 1: #Permet de déterminer le gagnant
		print("Le joueur NOIR remporte la partie!")
	else:
		print("Le joueur BLANC remporte la partie!")

def saisir_taille_plateau():
	t = -1
	while t not in [4,6,8]:
		t = int(input("Entrez la taille du plateau (4,6 ou 8): ")) #Redemande tant que l'utilisateur n'a pas saisi un chiffre qui est soit 4, 6 ou 8
	return t

def sauvegarder_partie(partie):
	file = open("sauvegarde_partie.json", "w") #Permet d'ouvrir un ficher

	json.dump(partie, file) #Enregistre la partie dans le fichier

def charger_partie():
	if path.exists("sauvegarde_partie.json"):
		file = open('sauvegarde_partie.json', 'r')
		partie = json.load(file)
		return partie
	else:
		print("Le fichier sauvegarde_partie.json n'existe pas.")

def othello():
	efface_term() #Efface le terminal
	print("=========== Bienvenue sur le jeu d'Othello ===============")
	while True:
		action = saisir_action(None) #Renvoi au menu avec pour seul possibilité de quitter, commencer ou charger une partie
		interprete_action(action, None)


othello()

def test_creer_partie():
	assert len(creer_partie(4)["plateau"]["cases"])==16 #Vérifie que la partie créé un plateau de taille 4 possèdant bien 16 cases
	assert len(creer_partie(6)["plateau"]["cases"])==36 #Vérifie que la partie créé un plateau de taille 6 possèdant bien 36 cases
	assert not len(creer_partie(8)["plateau"]["cases"])==45 #Vérifie que la partie créé un plateau de taille 8 ne possède pas seulement 45 cases

def test_saisie_valide():
	partie=creer_partie(4) 
	assert saisie_valide(partie, "b1") #Vérifie que les coordonnées "b1" sont bien valides et pose en un pion aux coordonnées sélectionnées 
	partie=creer_partie(8)
	assert saisie_valide(partie, "c4") #Vérifie que les coordonnées "c4" sont bien valides et pose en un pion aux coordonnées sélectionnées

def test_tour_jeu():
	partie=creer_partie(6)
	tour_jeu(partie) #On effectue un tour de jeu 
	print(partie) #Permet de vérifier que l'action a bien été effectuée

def test_saisir_action():
	partie=creer_partie(8)
	n = saisir_action(partie) #Permet de vérifier dans le menu si l'on peut effectuer une action, sous forme de nombre, comprise entre 0 et 4
	assert n>= 0 and n<= 4

def test_jouer():
	partie=creer_partie(4)
	partie = {"joueur": 1, "plateau": {"n": 4, "cases": [2, 2, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 0, 0]}} #partie presque finie
	jouer(partie) #Permet de jouer une partie et donc de vérifier que le jeu fonctionne

def test_saisir_taille_plateau():
	assert saisir_taille_plateau()==6 or saisir_taille_plateau()==4 or saisir_taille_plateau()==8#Permet de vérifier que la taille du tableau saisi par l'utilisateur, peut être modifiée en 4 ou 8

def test_sauvegarder_partie():
	partie=creer_partie(6)
	sauvegarder_partie(partie) #Vérifie que l'on peut sauvegarder une partie
	if path.exists("sauvegarde_partie.json"):
		file = open("sauvegarde_partie.json", "r")
		assert partie == json.load(file)

def test_charger_partie():
	partie = creer_partie(4)
	sauvegarder_partie(partie)
	part=charger_partie() #Vérifie que l'on peut charger la partie précédemment sauvegardée
	assert part == partie

if __name__ == "__main__":
    print("Démarrage du test de toutes les fonctions de la Partie 2...")

    test_creer_partie()
    print("     Fonction [ creer_partie ]:                 Valide")
    
    test_saisie_valide()
    print("     Fonction [ saisie_valide ]:                Valide")

    test_tour_jeu()
    print("     Fonction [ tour_jeu ]:                     Valide")

    test_saisir_action()
    print("     Fonction [ saisir_action ]:                Valide")

    test_jouer()
    print("     Fonction [ jouer ]:                        Valide")

    test_saisir_taille_plateau()
    print("     Fonction [ saisir_taille_plateau ]:        Valide")

    test_sauvegarder_partie()
    print("     Fonction [ sauvegarder_partie ]:           Valide")

    test_charger_partie()
    print("     Fonction [ charger_partie ]:               Valide")
