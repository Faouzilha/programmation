# Ecrire une fonction qu'on nommera volume qui prend en entrée trois nombres longueur, largeur 
# et hauteur (dans cet ordre) et qui renvoie le volume d'un pavé droit avec ces dimensions 
# si (oui) le volume est inférieur à 100, sinon on retoune -1



# Variables volume longueur, largeur, hauteur
# Debut
        # Fonction volume_pave <- longueur * largeur * hauteur

    # si volume_pave < 100 alors
        # retourner volume_pave

    # sinon 
        # retourner -1
# FinSi

def volume(longueur, largeur, hauteur):# fonction (args) calcul du volume
    volume_pave = longueur * largeur * hauteur
    
    # vérif si le volume est inférieur à 100
    if volume_pave < 100:
        return volume_pave
    else:
        return -1

# appel de la fonction
longueur_input = float(input("Entrez la longueur : "))
largeur_input = float(input("Entrez la largeur : "))
hauteur_input = float(input("Entrez la hauteur : "))

resultat = volume(longueur_input, largeur_input, hauteur_input)

if resultat != -1: # Si la valeur de la variable resultat n'est pas égale à -1, alors exécute le bloc de code suivant
    print("Le volume du pavé droit est :", resultat)
else:
    print("Le volume est supérieur ou égal à 100.")
