from Part1 import *

def pion_adverse(joueur):
    """ 
    Retourne l'entier correspondant à l'adversaire :
    - retourne 2 si joueur vaut 1,
    - retourne 1 si joueur vaut 2.
    Lève une erreur si joueur est différent de 1 et 2.
    """
    assert joueur == 1 or joueur == 2 # Lève une erreur si le joueur n'est pas le joueur 1 ou le joueur 2
    if joueur == 1:
        return 2 # Si le joueur est le joueur 1, retourne 2 qui correspond à son adversaire
    else:
        return 1 # Sinon retourne 1, correspond à l'adversaire du joueur 2 


def prise_possible_direction(p, i, j, vertical, horizontal, joueur):
    assert case_valide(p,i,j)
    tmp_j = j + horizontal
    tmp_i = i + vertical
    while case_valide(p, tmp_i,tmp_j) and get_case(p,tmp_i,tmp_j) == pion_adverse(joueur):
        tmp_i += vertical
        tmp_j += horizontal
        if case_valide(p, tmp_i, tmp_j) and get_case(p,tmp_i,tmp_j) == joueur:
            return True
    return False

def mouvement_valide(plateau, i, j, joueur):
    if get_case(plateau, i, j) != 0:
        return False
    else:
        for vertical in range(-1, 2):
            for horizontal in range(-1, 2):
                if prise_possible_direction(plateau, i, j, vertical, horizontal, joueur):
                    return True
    return False

def mouvement_direction(plateau, i, j, vertical, horizontal, joueur):
    """ Joue le pion du joueur à la case (i,j) si c'est possible."""
    #if mouvement_valide(plateau, i,j, joueur):
    tmp_i = i
    tmp_j = j
    while prise_possible_direction(plateau, tmp_i, tmp_j, vertical, horizontal, joueur):
        tmp_j += horizontal
        tmp_i += vertical
        set_case(plateau, tmp_i, tmp_j, joueur)

def mouvement(plateau, i,j, joueur):
    if mouvement_valide(plateau, i,j, joueur) and get_case(plateau, i, j) == 0:
        set_case(plateau, i, j, joueur)
        for v in range(-1,2):
            for h in range(-1, 2):
                if prise_possible_direction(plateau, i, j, v,h , joueur):
                    mouvement_direction(plateau, i,j, v,h, joueur)

def joueur_peut_jouer(plateau, joueur):
    n = plateau["n"]
    for i in range (n):
        for j in range(n):
            if get_case(plateau, i,j) == 0 and mouvement_valide(plateau,i,j, joueur):
                return True
    return False

def fin_de_partie(plateau):
    if joueur_peut_jouer(plateau, 1) and joueur_peut_jouer(plateau,2):
        return False
    else:
        return True

def gagnant(plateau):
    n = plateau["n"]
    point_1 = 0
    point_2 = 0
    for i in range(n):
        for j in range(n):
            case = get_case(plateau, i,j)
            if case == 1:
                point_1 += 1
            elif case == 2:
                point_2 += 1
    if point_2 > point_1:
        return 2
    elif point_1 > point_2:
        return 1
    else:
        return 0


"""
def test_pion_adverse():
    p=creer_plateau(6) #Crée un plateau de taille 6*6
    assert pion_adverse(2)==1 #Doit retourner True car l'adversaire du joueur 2 est le joueur 1
    assert pion_adverse(1)==2 #Doit retourner True car l'adversaire du joueur 1 est le joueur 2
    assert not pion_adverse(2)==2 #Doit retourner False car l'adversaire du joueur 2 n'est pas le joueur 2
    assert not pion_adverse(1)==1 #Doit retourner False car l'adversaire du joueur 1 n'est aps le joueur 1

def test_prise_possible_direction():
    p=creer_plateau(6) #Crée un plateau de taille 6*6
    assert prise_possible_direction(p,1,2,1,0,1) #Doit retourner True car on peut retourner un pion blanc en (2,2)
    assert prise_possible_direction(p,4,2,-1,0,2) #Doit retourner True car on peut retourner un pion noir en (3,2)
    assert not prise_possible_direction(p,5,3,-1,0,1) #Doit retourner False car on ne peut pas retourner de pion blanc en (4,3)
    
    p=creer_plateau(8) #Crée un plateau de taille 8*8
    assert not prise_possible_direction(p,3,4,-1,0,1) #Doit retourner False car on ne peut pas retouner de pion en (2,4)
    assert prise_possible_direction(p,4,5,0,-1,1) #Doit retourner True car on peut retourner un pion blanc en (4,4)
    assert prise_possible_direction(p,2,4,1,0,2) #Doit retourner True car on peut retourner un pion noir en (3,4)

def test_mouvement_valide():
    p=creer_plateau(6) #Crée un plateau de taille 6*6
    #assert mouvement_valide(p,2,4,2) #Doit retourner True car on peut retourner un pion noir en (2,3) en posant un pion blanc en (2,4)
    #assert not mouvement_valide(p,5,5,1) #Doit retourner False car on ne peut pas retourner de pion blanc en posant un pion noir en (5,5)
    assert mouvement_valide(p,3,1,2) #Doit retourner True car on peut retourner un pion blanc en (3,1) en posant un pion noir en (3,0)

    p=creer_plateau(8) #Crée un plateau de taille 8*8
    assert mouvement_valide(p,3,2,1) #Doit retourner True car on peut retourner un pion blanc en (3,3,) en posant un pion noir en(3,2)
    assert mouvement_valide(p,4,2,2) #Doit retourner True car on peut retourner un pion noir en (4,3) en posant un pion blanc en (4,2)
    set_case(p,5,3,1) #Change la valeur de la case en (5,3) pour que le pion devienne un pion du joueur 1
    assert mouvement_valide(p,6,2,2) #Doit retourner True car on peut retourner un pion noir en (5,3) en posant un pion blanc en (6,2)

def test_mouvement_direction():
    p=creer_plateau(4) #Crée un plateau de taille 4*4
    mouvement_direction(p,1,3,0,-1,2) #Le pion du joueur 2 effectue un mouvement vers la gauche depuis la case (1,3)
    assert get_case(p,1,2)==2 #Vérifie que le pion de la case (1,2) est bien devenu un pion blanc, doit retourner True
    mouvement_direction(p,2,0,0,1,2) #Le pion du joueur 2 effectue un mouvement vers droite depuis la case (2,0)
    assert get_case(p,2,1)==2 #Vérifie que le pion de la case (2,1) est bien devenu un pion blanc, doit retourner True

    p=creer_plateau(6) #Crée un plateau de taille 6*6
    mouvement_direction(p,3,1,0,1,2) #Le pion du joueur 2 effectue un mouvement vers la droite depuis la case (3,1)
    assert get_case(p,2,2)==2 #Vérifie que le pion de la case (2,2) est bien devenu un pion blanc, doit retourner True
    mouvement_direction(p,2,1,0,1,1) #Le pion du joueur 1 esffectue un mouvment vers la droite depuis la case (2,1)
    assert get_case(p,2,2)==1 #Vérifie que le pion de la case (2,2) est bien devenu un pion noir, doit retourner True

def test_mouvement():
    p = creer_plateau(6) #Crée un plateau de taille 6*6
    mouvement(p,3,1,2) #Effectue le mouvement du pion du joueur 2 en (3,1) 
    assert get_case(p,3,2)==2 #Vérifie que la case (3,2) posède bien un pion du joueur 2, doit retourner True

    p=creer_plateau(8) #Crée un plateau de taille 8*8
    mouvement(p,4,2,2) #Effectue le mouvement du pion du joueur 2 en (4,2) 
    assert get_case(p,4,4)==2 #Vérifie que la case (4,4) posède bien un pion du joueur 2, doit retourner True
    assert not get_case(p,4,4)==1 #Vérifie que la case (4,4) ne possède pas un pion du joueur 1, doit retourner False

def test_joueur_peut_jouer():
    p=creer_plateau(4) #Crée un plateau de taille 4*4
    for i in range(0,4): #Permet de remplir les cases vides du plateau par des cases contenant les pions du joueur 2
        for j in range(0,4):
            set_case(p,i,j,2)
    assert not joueur_peut_jouer(p,2) #Doit retourner False car le joueur 2 ne peut plus jouer puisque la plupart des cases du plateau possède des pions du joueur 1
    assert not joueur_peut_jouer(p,1) #Doit retourner False car le joueur 1 ne peut plus jouer puisque la plupart des cases du plateau possède ses pions

    p=creer_plateau(6)
    set_case(p,2,4,1)
    assert joueur_peut_jouer(p,1) #Doit retourner True car le joueur 1 peut encore jouer
    assert joueur_peut_jouer(p,2) #Doit retourner True car le joueur 2 peut encore jouer


def test_fin_de_partie():
    p=creer_plateau(4) #Crée un plateau de taille 4*4
    for i in range(0,4): #Permet de remplir les cases vides du plateau par des cases contenant les pions du joueur 2
        for j in range(0,4):
            set_case(p,i,j,2)
    assert fin_de_partie(p) #Doit retourner True car aucun joueur ne peut jouer puisque le palteau est remplit
    
    p=creer_plateau(8) #Crée un plateau de taille 8*8
    set_case(p,1,1,2) #Change la valeur de la case en pion blanc (pion du joueur 2)
    assert not fin_de_partie(p) #Doit retourner False car au moins un joueur peut encore jouer

def test_gagnant():
    p=creer_plateau(6) #Crée un plateau de taille 6*6
    set_case(p,3,2,2)   #
    set_case(p,2,3,2)   #On modifie les pion noir en pion blanc et on ajoute un pion blanc pour qu'il y ai plus de pion blanc que de pion noir
    set_case(p,5,5,2)   #
    assert gagnant(p) #Doit retourner True car le joueur 2 à plus de pion que le joueur 1

    p=creer_plateau(8) #Crée un plateau de taille 8*8
    assert not gagnant(p) #Doit retourner False car le joueur 1 à autant de pion que le joueur 2


if __name__ == "__main__":
    print("Démarrage du test de toutes les fonctions de la Partie 2...")

    test_pion_adverse()
    print("     Fonction [ pion_adverse ]:                 Valide")
    
    test_prise_possible_direction()
    print("     Fonction [ prise_possible_direction ]:     Valide")

    test_mouvement_valide()
    print("     Fonction [ mouvement_valide ]:             Valide")

    test_mouvement_direction()
    print("     Fonction [ mouvement_direction ]:          Valide")

    test_mouvement()
    print("     Fonction [ mouvement ]:                    Valide")

    test_joueur_peut_jouer()
    print("     Fonction [ joueur_peut_jouer ]:            Valide")

    test_fin_de_partie()
    print("     Fonction [ fin_de_partie ]:                Valide")

    test_gagnant()
    print("     Fonction [ gagnant ]:                      Valide")

"""