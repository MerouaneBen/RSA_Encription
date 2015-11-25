from convertisseurs import liste_entiers_a_chaine, chaine_a_liste_entiers


def est_premier(nombre):
    """Détermine si un nombre est premier.

    Args:
        nombre (int): Le nombre à vérifier.

    Returns:
        bool: True si le nombre est premier, et False autrement.

    """
    # TODO: Programmez cette fonction en retirant l'instruction pass (qui ne fait rien) et en y
    # TODO: ajoutant votre code.

    # on déclare la variable resultat comme True
    resultat = True
    i = 2

    if nombre <= 0 or nombre == 1: # on exclut les valeurs négatifs, 0 et 1
        resultat = False
    else:
        # quant la valeur de i est  inférieur ou égale  au nombre - 1
        while i <= nombre - 1:
                if nombre % i == 0:  # on teste si le nombre a un diviseur
                    resultat = False   # si on trouve un diviseur on affiche le résultat False

                i += 1

    return resultat



def prochain_premier(nombre):
    """Trouve le plus petit nombre premier, qui est plus grand ou égal au nombre reçu en argument.

    Args:
        nombre (int): Le plus petit nombre à considérer.

    Returns:
        int: Le nombre premier trouvé.

    """
    # TODO: Programmez cette fonction en retirant l'instruction pass (qui ne fait rien) et en y
    # TODO: ajoutant votre code.

    #  pour ce programme on va se baser sur la premiere fonction est_premier(nombre)

    while est_premier(nombre) == False:  # on teste à l'aide de la premiere fonction, si le nombre est premier,
        nombre = nombre +1   # si on trouve que le nombre introduit n'est pas premier, on l'incrémente de 1

    return nombre



def facteurs_premiers(nombre):
    """Retourne la décomposition en produit de facteurs premiers du nombre reçu en argument.

    Args:
        nombre (int): Le nombre à factoriser.

    Returns:
        list: La liste des facteurs premiers, en ordre croissant.

    """
    # TODO: Programmez cette fonction en retirant l'instruction pass (qui ne fait rien) et en y
    # TODO: ajoutant votre code.

    liste_Facteur = []  # on déclare une liste_Facteur
    n = 2
    while n <= nombre: # On  commence la boucle qui calcule les facteurs premiers
        if nombre % n == 0: # si n est un diviseur du nombre on continu
            liste_Facteur.append(n) # on enregistre le la valeur de n dans la liste_Facteur
            result = int(nombre/n) # on calcule la valeur de la division
            nombre = int(result) # on affecte à la variable Nombre le resultat de la division sur n
        else :
            n =n+1

    return liste_Facteur


def sont_copremiers(nombre_1, nombre_2):
    """Détermine si deux nombres sont "co-premiers", c'est à dire s'ils ne partagent aucun facteur premier différent de 1.
    Vous devinerez qu'il serait judicieux d'appeler deux fois la fonction facteurs_premiers (qui retourne une liste de
    facteurs), puis de comparer les deux listes reçues entre elles.

    Args:
        nombre_1 (int): Le premier nombre.
        nombre_2 (int): Le second nombre.

    Returns:
        bool: True si les deux nombres sont copremiers, False autrement.

    """
    # TODO: Programmez cette fonction en retirant l'instruction pass (qui ne fait rien) et en y
    # TODO: ajoutant votre code.

    liste_Facteur_nombre_1 = facteurs_premiers(nombre_1) # on remplie cette liste par les facteur premiers du nombre_1
    liste_facteur_nombre_2 = facteurs_premiers(nombre_2) # on remplie cette liste par les facteurts premiers du nombre_2
    liste_de_test = []  # liste vide qui va contenir les facteurs premier partagés entre les deux nombres

    for membre in liste_Facteur_nombre_1:    # on fait une boucle for pour chaque élement de la liste des facteurs du nombre_1
        if membre in liste_facteur_nombre_2:    # on test si  le nomnbre est dans la liste des facteurs du nombre_2
            liste_de_test.append(membre)    #  quand on trouve un element oartagé dans les deux listes, on l'ajoute dans a liste de teste

        if liste_de_test == []: # On fait un test sur la liste_test
            resultat_comparaison = True    # si elle est vide, on affiche le résultat True les deux memebres sont co_equiper
        else:
            resultat_comparaison = False   # si elle n'est pas vide, on affiche le resultat  False, les deux membres ne sont pas co_equiper

    return resultat_comparaison


def sont_congruents(nombre_1, nombre_2, modulo):
    """Détermine si deux nombres sont "congruents", c'est à dire si les deux nombres
    sont égaux une fois l'opération modulo appliquée (pour un certain modulo).
    Autrement dit, les deux nombres sont congruents (modulo n) s'ils ont le même reste
    de division entière par n.

    Args:
        nombre_1 (int): Le premier nombre.
        nombre_2 (int): Le second nombre.
        modulo (int): Le modulo à utiliser pour vérifier la congruence.

    Returns:
        bool: True si les deux nombres sont congruents (étant donné le modulo reçu), False autrement.

    """
    # TODO: Programmez cette fonction en retirant l'instruction pass (qui ne fait rien) et en y
    # TODO: ajoutant votre code.

    valeur_1 = nombre_1 % modulo    # on attribue la valeur du résultat du modulo à la variable valeur_1
    valeur_2 = nombre_2 % modulo    # on attribue la valeur du résultat du modulo à la variable valeur_2

    if valeur_1 == valeur_2:  # on teste si les deux valeurs sont égaux
        restltat_congurence = True
    else:
        restltat_congurence = False

    return restltat_congurence


def chiffrer_dechiffrer(nombre, cle):
    """Chiffre (encrypte) ou déchiffre un nombre à l'aide une clé (publique ou privée), en utilisant la méthode RSA. Si
    une clé publique est reçue, le résultat de la fonction sera un nombre chiffré. Si une clé privée est reçue, le
    résultat sera le nombre original. Voir l'énoncé pour connaître les opérations mathématiques à faire ici.

    Args:
        nombre (int): Le nombre à chiffrer ou déchiffrer.
        cle_publique (list): Une liste de deux entiers: le module de chiffement et l'exposant de chiffrement (ou de
            déchiffrement).

    Warning:
        Le nombre ne peut pas être plus grand que le module de chiffrement, sinon l'algorithme RSA ne fonctionnera pas.
        Vous pouvez utiliser l'instruction assert pour vous en assurer, mais lors de la correction nous n'utiliserons
        que des nombres/clés compatibles.

    Returns:
        int: L'entier chiffré ou déchiffré.

    """
    # TODO: Programmez cette fonction en retirant l'instruction pass (qui ne fait rien) et en y
    # TODO: ajoutant votre code.

    resultat_cheff_decheff =  pow(nombre,cle[1],cle[0]) # on calcule dla valeur de chiff et dechiff

    return resultat_cheff_decheff


def chiffrer_fichier(nom_fichier_entree, nom_fichier_sortie, cle_publique):
    """À l'aide d'une clé de chiffrement (clé publique), ouvre un fichier texte, chiffre le contenu,
    puis écrit le résultat (liste de nombres) dans un autre fichier. Notez que cette fonction ne
    retourne rien: son résultat est l'écriture d'un fichier sur le disque.

    Étapes à suivre:
        1. Ouvrir le fichier d'entrée et en lire le contenu.
        2. Convertir le contenu (chaîne) en liste d'entiers, en utilisant la fonction chaine_a_liste_entiers.
        3. Pour chaque entier de cette liste, chiffrer le nombre à l'aide de la clé publique.
        4. Écrire dans le fichier de sortie chacun des nombres. Utilisez une ligne différente pour écrire
            ces nombres.

    Args:
        nom_fichier_entree (str): Le nom du fichier contenant le texte à chiffrer.
        nom_fichier_sortie (str): Le nom du fichier où écrire le résultat du chiffrement.
        cle_publique (list): Une liste de deux nombres: le module de chiffrement et l'exposant de chiffrement.

    """
    # TODO: Programmez cette fonction en retirant l'instruction pass (qui ne fait rien) et en y
    # TODO: ajoutant votre code.

    fichier_sortie = open(nom_fichier_sortie, 'w')  # on ouvre le document de sortie en mode écriture
    fichier_entree = open(nom_fichier_entree, 'r')  # on ouvre le docuement d'entré en mode lecture

    contenu = fichier_entree.read() # on lit le contenu du docuement d'entré
    code = chaine_a_liste_entiers(contenu) # on convertit la chaine de carectère en liste d'entiers

    for element in code:    # on chiffre chaque élement de la liste d'entiers a l'aide de la clé_publique fourni
        code_chiffrement=chiffrer_dechiffrer(element,cle_publique)
        fichier_sortie.write((str(code_chiffrement)+'\n'))  # on écrit les codes chiffrés dans fichier de sortie

    fichier_entree.close()
    fichier_sortie.close()


def dechiffrer_fichier(nom_fichier_entree, cle_privee):
    """À l'aide de la clé de déchiffrement (clé privée), déchiffrer le contenu d'un fichier (préalablement chiffré à
    l'aide de la fonction chiffrer_fichier) et retourner la chaîne résultante.

    Étapes à suivre:
        1. Ouvrir le fichier contenant le message codé, et en lire le contenu. Chaque ligne devrait contenir un entier.
        2. Pour chacune de ces lignes (chiffres), déchiffrer le nombre en utilisant la clé privée. Récupérer le
            dans une liste de nombres déchiffrés.
        3. Transformer cette liste en chaîne de caractères, en utilisant la fonction liste_entiers_a_chaine.
        4. Retourner cette chaîne.

    Args:
        nom_fichier_entree (str): Le nom du fichier où lire le message chiffré.
        cle_privee (list): Une liste de deux entiers: le module de chiffrement et l'exposant de déchiffrement.

    Returns:
        str: La chaîne de caractères déchiffrée.

    """
    # TODO: Programmez cette fonction en retirant l'instruction pass (qui ne fait rien) et en y
    # TODO: ajoutant votre code.

    fichier_entree= open(nom_fichier_entree, 'r') # on ouvre le fichier d'entré qui contient le message chiffré en mode r
    liste_nombre_dechiffre = [] # on déclare une liste vide pour les nombre déchiffré
    contenu = fichier_entree.readline() # on commence à lire la premiere ligne du fichier

    while contenu != "": # on fait une boucle pour lire dechiffré tous le nombre du fichier

        nombre_dechiffre = chiffrer_dechiffrer(int(contenu),cle_privee)
        liste_nombre_dechiffre.append(nombre_dechiffre) # on enregistre le nombre déchiffrés dans une liste
        contenu = fichier_entree.readline() # on lit le chiffre suivant

    message_dechiffre = liste_entiers_a_chaine(liste_nombre_dechiffre) # on convertis les chiffres en un message de chaine

    fichier_entree.close()
    return message_dechiffre

def generer_paire_de_cles(minimum_premier_1=1000, minimum_premier_2=2000):
    """Cette fonction, dont le code vous est fourni, permet de générer deux clés: une clé de chiffrement
    (clé publique), et une clé de déchiffrement (clé privée). Cette fonction utilise d'autres fonctions que vous
    avez à programmer, il est donc normal qu'elle ne fonctionne pas tant que vos propres fonctions soient terminées.
    Utilisez le module test_rsa.py (fourni) pour tester vos propres fonctions d'abord, avant de tenter d'utiliser
    la présente fonction.

    Rendez-vous sur la page Wikipédia de la cryptographie RSA pour plus d'informations sur ces étapes!

    Warning:
        Dans la vraie vie, il faudrait utiliser des nombres premiers BEAUCOUP plus grands, et rendre ce processus
        aléatoire (on ne veut pas générer plusieurs fois la même clé).

    Args:
        minimum_premier_1 (int, optional): Le plus petit nombre à considérer comme premier nombre premier.
        minimum_premier_2 (int, opitonal): Le plus petit nombre à considérer comme second nombre premier.

    Returns:
        list: Une liste de deux clés, qui elles-même sont des listes de deux nombres. Récupérez le résultat de cette
        fonction comme suit :
            cle_privee, cle_publique = generer_paire_de_cles()

    """

    # On choisit deux "grands" nombres premiers.
    p = prochain_premier(minimum_premier_1)
    q = prochain_premier(minimum_premier_2)

    # On calcule le module de chiffrement n, puis l'indicatrice d'Euler de p et q.
    module = p * q
    indicatrice = (p - 1) * (q - 1)

    # On cherche un exposant de chiffrement e tel que e et l'indicatrice sont copremiers. On commence avec une valeur
    # suffisamment petite (17), et si celle-ci ne fonctionne pas, on continue la recherche.
    exposant_chiffrement = 17
    while exposant_chiffrement < indicatrice:
        if sont_copremiers(exposant_chiffrement, indicatrice):
            break
        exposant_chiffrement += 1

    # On vérifie qu'on a bel et bien trouvé un exposant!
    assert exposant_chiffrement < indicatrice, "Erreur: impossible de trouver un nombre copremier."

    # On cherche un exposant de déchiffrement d qui tel que d * e est congruent à 1, modulo l'indicatrice.
    exposant_dechiffrement = 2
    while exposant_dechiffrement < indicatrice:
        if sont_congruents(exposant_dechiffrement * exposant_chiffrement, 1, indicatrice):
            break
        exposant_dechiffrement += 1

    assert exposant_dechiffrement < indicatrice, "Erreur: impossible de trouver un nombre congruent."

    # On crée les clés publique et privée avec nos nombres, et on les retourne.
    cle_publique = [module, exposant_chiffrement]
    cle_privee = [module, exposant_dechiffrement]

    return cle_privee, cle_publique


if __name__ == '__main__':
    # Voici le point d'entrée principal du TP, le bout de code suivant va afficher le contenu du fichier secret.txt fourni.
    # La clé utilisée, c'est [82304707819, 17] fourni aussi dans l'énoncé!


    # TODO: Une fois le code ci-haut fonctionnel et que vous êtes en mesure de chiffrer et déchiffrer le message
    # TODO: clair fourni avec l'énoncé (fichier_a_chiffrer.txt), supprimez le code ci-haut et écrivez le code
    # TODO: nécessaire pour déchiffrer et afficher le contenu du fichier secret.txt fourni avec l'énoncé.
    # TODO: Utilisez "votre" clé privée, donnée dans l'énoncé du TP.

    print ('Déchiffrement fichier secret en cours...\n')
    message_secret = dechiffrer_fichier('secret.txt', [82304707819, 17])
    print("Message déchiffré:")
    print("---------------------------------------------------------------------")
    print(message_secret)
    print("---------------------------------------------------------------------\n\n\n")


    print ("Note: défi casse code ")
    print("---------------------------------------------------------------------")
    print(""" J'ai essayé deux approches différentes pour calculer l'exposant_dechiffrement, ci-dessous les détails:

la première approche :
    J'ai commencé par calculer le p et le q :
    Je sais que le module  n = p * q,
      1 - J'ai commencé par calculer le sqrt(n)
      2 - J'ai trouvé le diviseur premier de n, donc le p = 123457
      3 - J'ai calculé ensuite le q = 666667
    Pour trouver l'exposant manquant, j'ai pensé tout simplement à exécuter la fonction generer_paire_de_cles avec
    mes deux nouvelles valeurs p et q, mais le temps d'exécution était très long, j'ai patienté environ 7h
    sans avoir de résultat.

    Donc la question que je me pose,\033[1m ça vous a pris combien de temps pour générer les deux clés avec cette fonction?\033[0m

La deuxiement approche :
Après ce temps d'attente, j'ai pensé de faire la rétro-ingénierie de la fonction generer_paire_de_cles
    1 - J'ai analysé le code pour comprendre son fonctionnement et j'ai développé un script qui calcule
     l'exposant_dechiffrement manquant.
        * Ceci m'a pris moins d'une heure pour le résoudre, et le code s'exécute dans moins d'une seconde!;)
    """)
# Je mets ci-dessous le script pour calculer l'exposant_dechiffrement :
    n = 1  # je déclare n, ceci est le multiplicateur du modulo
# on sait que le modulo c'est le nombre entier restant d'une opération de division
# pour avoir avoir un modulo == 1, il faut que le nombre divisé soit supérieur du nombre diviseur de seulement 1
modulo = 82303917696 # on déclare une variable modulo

# on commence notre test, on calcule le nombre a qui donne le résultat d'un modulo 1

a = modulo # pour commencer on attribue une valeur initiale à notre variable a, c'est la même que la variable modulo

# on boucle pour avoir la valeur de a qui nous donne la valeur 0 sur un modulo 17
while a % 17 != 0:
    a = (modulo * n)+1
    n +=1
print("La valeur de l'exposant_dechiffrement =", int(a/17))
print("""Les deux clés utilisés sont :
     \033[1mcle_privee = [82304707819, 48414069233]
     cle_publique = [82304707819, 17]\033[0m
        """)
print('Fin de Note!\n'+"---------------------------------------------------------------------")
print ('\n'+'{0:20}'.format(''),'{:*^30}'.format('Merci!'))

