from termcolor import cprint, colored
from time import time

def indice_valide(plateau, indice):
	"""
	Retourne True si l'indice existe dans le tableau Case
	"""
	n = plateau["n"] #On récupère la taille du plateau
	if indice < 0 or indice > (n-1):
		#Si l'indice (i ou j) n'est pas compris entre 0 et la taille-1 il est faux
		return False
	else:
		return True

def case_valide(plateau, i, j):
	""""
	Retourne True si I et J sont des indices valides
	"""
	if indice_valide(plateau,i) and indice_valide(plateau,j):
		#On verifie que i et j sont tous les deux des indices valides
		#Si c'est le cas la case est valide
		return True
	else:
		return False

def get_case(plateau, i, j):
	"""
	Retourne la case du tableau
	et lève une erreur si cette case n'existe pas 
	"""
	#On verifie que la case est valide avant toute chose
	assert case_valide(plateau, i, j)

	#si c'est le cas
	n = plateau["n"]
	#On determine l'indice du tableau correspondant à la case (i j)
	position = (i*n)+j
	#Et on renvoit la valeur de cette case
	return plateau["cases"][position]
	
def set_case(plateau, i, j, val):
	"""
	Affecte la valeur val dans la case (i,j). Erreur si (i,j) n'est pas une case
    ou si val n'est pas entre 0 et 2.
    Met aussi à jour le nombre de cases libres (sans pion).
    """

    #On verifie que la case existe
	assert case_valide(plateau, i, j)
	#Ainsi que la nouvelle valeur est valide
	assert val>=0 and val <=2

	n = plateau["n"]
	#On determine l'indice du tableau correspondant à la case (i j)
	position = (i*n)+j
	#On assigne la valeur a la casse correspondante
	plateau["cases"][position] = val

def creer_plateau(n):
	""" Retourne une nouvelle partie. Lève une erreur si n est différent de 4, 6 ou 8.
    Une partie est un dictionnaire contenant :
    - n : valeur passée en paramètre
    - cases : tableau de n*n cases initialisées
    """

	#On verifie que la taille du tableau que l'on veut creer est bonne
	assert n==4 or n==6 or n==8
	#On initialise le plateau en tant que dictionnaire
	plateau = dict()
	#On attribue au premier indice "n" la taille n du plateau
	plateau["n"] = n

	plat = [] #liste temporaire pour simplifier la syntaxe.
			  # -> plat.append(x) au lieu de plateau["cases"].append(x)
	taille = n*n #nombre de case du plateau
	i = 0
	while i < taille:
		if i == taille/2 - (n/2) or i == taille/2 + (n/2)-1:
			#Si i correspont au centre haut-droite du plateau
			#Ou au centre bas-gauche du plateau
			plat.append(1) #On attribue 1
		elif i == taille/2 - (n/2)-1 or i == taille/2 + (n/2):
			#Si i correspont au centre haut-gauche du plateau
			#Ou au centre bas-droite du plateau
			plat.append(2) #On attribue 2
		else:
			#Sinon c'est que c'est une case qui n'est pas au centre
			plat.append(0) #On attribue alors 0
		i += 1
	plateau["cases"] = plat #On assigne plat a l'indice "cases" du dictionnaire plateau 
	return plateau #On renvoit le plateau creer


def afficher_plateau(plateau):
	n = plateau["n"]
	i = 0 #Pour parcourir le tableau de cases
	a = 0 #Pour compter les lignes affichées
	lenght = len(plateau["cases"]) #Le nombre de cases
	plat = plateau["cases"] #tableau temporaire pour simplifier la syntaxe

	print("-"*((n*8)+1)) #Ligne de délimitation supérieure qu'on affiche au début
	#Afin que l'affichage du plateau semble carré on affiche des ligne "vide"
	print("|       "*n,end="|\n") #Celle-ci est la première
	while i < lenght:
		if a == n:
			#Si on a afficher tous les caractères d'une ligne
			print("|") #On affiche la délimitation de côté pour la fin de la ligne
			print("|       "*n,end="|\n") # On ré-affiche une ligne "vide"
			print("-"*((n*8)+1)) #On affiche la délimitation entre les cases affichées
			print("|       "*n,end="|\n") #Et on affiche une seconde fois une ligne "vide" 
										#pour la ligne de cases qui va suivre
			a = 0 #On remet a=0 car on recommence une nouvelle ligne
		print("|",end='')#On affiche la délimitation de côté pour le début de la ligne
		if plat[i] == 1: print("   N   ",end='') #ce qu'on affiche si le pion est 1 (joueur1)
		elif plat[i] == 2: print("   B   ",end='')# ce qu'on affiche si le pion est 2 (joueur2)
		else: print('       ',end='') #Si c'est 0 on affiche une case vide
		a += 1 # a+= 1 car on a affiché une nouvelle case
		i += 1 #Pour parourir toutes les cases

	print("|")#On affiche la délimitation de côté pour la fin de la ligne
	print("|       "*n,end="|\n") # On ré-affiche une ligne "vide"
	print("-"*((n*8)+1))#On affiche la délimitation inférieure de la fin du plateau

def gen_line(n, color):
	"""
	Genere une ligne "vide" et cadrillée pour completer l'affichage du plateau
	"""
	line = "" # On creer une ligne vide
	i = 0
	#ici on creer notre deuxieme couleur qui sera l'inverse de la première
	if color == "on_green":
		color2 = "on_blue" 
	else:
		color2 = "on_green"

	#On genere la ligne en question
	while i < n:
		#On ajoute un espace coloré 
		line += colored("       ", "white", color)
		#on inverse les couleur pour obtenir le cadrillage (ou damier) voulu
		color, color2 = color2, color
		i += 1
	#On renvoit la ligne
	return " "+line

def afficher_plateau_colore(plateau):
	n = plateau["n"] #on stocke la taille
	plat = plateau["cases"] #tableau contenant les cases pour simplifier la syntaxe
	color1 = 'on_green'
	color2 = 'on_blue'

	#On affiche la premiere ligne avec les numero
	i = 1
	print(" ",end='')#on decale de 1 espace pour la propreté
	while i <= n:
		print("   "+str(i)+"   ", end='')
		i += 1
	print() #Retour a la ligne apres

	tmp_line1 = gen_line(n, color2) #On genere la premiere ligne intermédiaire
	tmp_line2 = gen_line(n, color1) #On genere la seconde ligne intermediaire
	i=0 # pour compter les cases
	a = 0 # pour compter les lignes
	taille = n*n #le nombre de cellule
	nplat = [] # nouveau plateau générer
	line = "" #ligne temporaire qui sera rajouter a nplat
	letter = 97 #la lettre "a" qui s'incrementera ensuite
	# On genere le plateau que l'on veut afficher
	while i < taille:
		a += 1
		if plat[i] == 0:
			 #ce qu'on affiche si le pion est 0 (case vide)
			line += colored("       ", "white", color1)
		elif plat[i] == 1:
			 #ce qu'on affiche si le pion est 1 (joueur1)
			line += colored("  000  ", "grey", color1)
		else:
			# ce qu'on affiche si le pion est 2 (joueur2)
			line += colored("  000  ", "white", color1)
		i += 1
		if a == n:
			#Si la ligne est terminée
			#On inverse les lignes intermédiaires qui sont vide
			tmp_line1, tmp_line2 = tmp_line2, tmp_line1
			a = 0 
			nplat.append(tmp_line1) # On affiche une ligne vide
			nplat.append(chr(letter)+line) #On affiche la ligne generer juste avant
			nplat.append(tmp_line1) # On ré-affiche la ligne intermédiaire
			letter += 1 #On incremente la lettre par ex: a deveint b, b devient c, etc
			line = "" #on remet la ligne temporaire a nulle
		else:
			color1, color2 = color2, color1 #on echange les couleur si il n'y a pas de retour a la ligne

	#On affiche le plateau colore
	for l in nplat:
		print(l)

def test_indice_valide():
    p = creer_plateau(4)
    assert indice_valide(p,0) # doit retourner True car 0 est valide
    assert indice_valide(p,3) # doit retourner True car 3 est valide
    assert not indice_valide(p,-1) # doit retourner False car -1 n'est pas valide
    assert not indice_valide(p,4) # doit retourner False car 4 n'est pas valide (si 4 cases : 0, 1, 2, 3)
    p = creer_plateau(6)
    assert indice_valide(p,4) # doit retourner True car on a maintenant 6 cases
    assert indice_valide(p,5) # doit retourner True car on a maintenant 6 cases
    assert not indice_valide(p,6) # doit retourner False  car les indices valides vont de 0 à 5
    return True

def test_case_valide():
    p = creer_plateau(6)
    assert case_valide(p, 0, 0) # doit retourner True car la case 0,0 existe 
    assert case_valide(p, 5, 5) # doit retourner True car la case 5,5 correspond à la dernière case 
    assert not case_valide(p, 7, 7) # doit retourner False car la case 7,7 n'existe pas 
    p = creer_plateau(8)
    assert case_valide(p, 0, 0) # doit retourner True car la case 0,0 existe 
    assert case_valide(p, 3, 3) # doit retourner True car la case 3,3 existe
    assert not case_valide(p, 8, 8) # doit retourner False car la case 8,8 n'existe pas
    return True

def test_get_case():
    p = creer_plateau(6)
    assert get_case(p, 0, 0) == 0 # doit retourner 0 
    assert get_case(p, 5,5) == 0 # doit retourner 0
    assert get_case(p, 2, 3) == 1 # doit retourner 1
    assert get_case(p, 3, 3) == 2 # doit retourner 2
    p = creer_plateau(8)
    assert get_case(p, 0, 0) == 0 # doit retourner 0
    assert get_case(p, 7,7) == 0 # doit retourner 0
    assert get_case(p, 3, 3) == 2 #doit retourner 2
    assert get_case(p, 4, 3) == 1 # doit retourner 1

def test_set_case():
    p = creer_plateau(6)
    set_case(p, 0, 0, 1) # on attribut la valeur 1 à la case 0,0
    assert get_case(p, 0, 0) == 1  # on vérifie que la case 0,0 renvoie la valeur 1, doit retourner 1
    set_case(p, 5, 5, 2) # on attribut la valeur 2 à la case 5,5
    assert get_case(p, 5, 5) == 2 # on vérifie que la case 5,5 renvoie la valeur 2, doit retourner 2
    p = creer_plateau(8)
    set_case(p, 0, 0, 1) # on attribut la valeur 1 à la case 0,0
    assert get_case(p, 0, 0) == 1 # on vérifie que la case 0,0 renvoie la valeur 1, doit retourner 1 
    set_case(p, 7,7, 2) # on attribut la valeur 2 à la case 7,7
    assert get_case(p, 7, 7) == 2 # on vérifie que la case 7,7 renvoie la valeur 1, doit retourner 2

def test_creer_plateau():
    p = creer_plateau(6)
    assert p["n"] == 6 # vérifie qu'on peut créer un tableau 66
    assert p["cases"][0] == 0 # vérifie que la case 0 contient la valeur 0, doit retourner True 
    assert p["cases"][35] == 0 # vérifie que la case 35 ne contient pas de valeur, doit retourner True 
    assert p["cases"][14] == 2 # vérifie que la case 14 contient un pion blanc car elle correspond à la case centrale haute gauche, doit retourner True
    assert p["cases"][15] == 1 # vérifie que la case 15 contient un pion noir car elle correspond à la case centrale haute droite, doit retourner True
    p = creer_plateau(4)
    assert p["n"] == 4 # vérifie qu'on peut créer un tableau 44
    assert p["cases"][6] == 1 # vérifie que la case 6 contient un pion noir car elle correspond à la case centrale haute droite, doit retourner True
    assert p["cases"][5] == 2 # vérifie que la case 5 contient un pion blanc car elle correspond à la case centrale haute gauche, doit retourner True
    assert p["cases"][0] == 0 # vérifie que la case 0 contient la valeur 0, doit retourner True 
    assert p["cases"][15] == 0 # vérifie que la case 15 ne contient pas de valeur, doit retourner True
    p = creer_plateau(8)
    assert p["n"] == 8 # vérifie qu'on peut créer un tableau 8*8
    assert p["cases"][27] == 2 # vérifie que la case 27 contient un pion blanc car elle correspond à la case centrale haute gauche, doit retourner True
    assert p["cases"][28] == 1 # vérifie que la case 28 contient un pion noir car elle correspond à la case centrale haute droite, doit retourner True
    assert p["cases"][0] == 0 # vérifie que la case 0 contient la valeur 0, doit retourner True 
    assert p["cases"][63] == 0 # vérifie que la case 63 ne contient pas de valeur, doit retourner True

def test_afficher_plateau():
	p = creer_plateau(6)
	i = 0 # pour parcourir les cases
	j1 = 1 # joueur 1
	j2 = 2 #joueur 2
	while i < 36:
		# On consitue le plateau d'une alternance de pion noir et blanc
		p["cases"][i] = j1
		i += 1
		j1, j2 = j2, j1
	#On affiche celui-ci pour verifier le resultat
	afficher_plateau(p)
	choix =''
	print("Le plateau suivant commence par un pion Noir et se termine par un pion Blanc.")
	print("La suite est constituée d'une alternance des ces deux pions")
	print("Si c'est bien le cas et que le plateau semble affiché correctement, veuillez repondre par un 'O' pour oui.")
	choix = input().upper()
	assert choix == 'O' #si le choix est bien Oui pour dire que l'affichage c'est bien passé

def test_afficher_plateau_colore():
	p = creer_plateau(6)
	i = 0 # pour parcourir les cases
	j1 = 1 # joueur 1
	j2 = 2 #joueur 2
	while i < 36:
		# On consitue le plateau d'une alternance de pion noir et blanc
		p["cases"][i] = j1
		i += 1
		j1, j2 = j2, j1
	#On affiche celui-ci pour verifier le resultat
	afficher_plateau_colore(p)
	choix =''
	print("Le plateau suivant commence par un pion Noir et se termine par un pion Blanc.")
	print("La suite est constituée d'une alternance des ces deux pions")
	print("Si c'est bien le cas et que le plateau semble affiché correctement, veuillez repondre par un 'O' pour oui.")
	choix = input().upper()
	assert choix == 'O' #si le choix est bien Oui pour dire que l'affichage c'est bien passé

if __name__ == "__main__":
	p = creer_plateau(4)
	afficher_plateau_colore(p)
	p = creer_plateau(6)
	afficher_plateau_colore(p)
	p = creer_plateau(8)
	afficher_plateau_colore(p)

	print("Démarrage du test de toutes les fonctions de la Partie 1...")
	test_indice_valide()
	print("		Fonction [ indice_valide ]:           Valide")
	
	test_case_valide()
	print("		Fonction [ case_valide ]:             Valide")

	test_get_case()
	print("		Fonction [ get_case ]:                Valide")

	test_set_case()
	print("		Fonction [ set_case ]:                Valide")

	test_creer_plateau()
	print("		Fonction [ creer_plateau ]:           Valide")

	test_afficher_plateau()
	print("		Fonction [ afficher_plateau ]:        Valide")

	test_afficher_plateau_colore()
	print("		Fonction [ afficher_plateau_colore ]: Valide")