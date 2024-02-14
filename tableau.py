# tableau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# On considère T un tableau non trié de n entiers.
# 1. Écrivez un algorithme qui calcule la somme des éléments de T.
# 2. Écrivez un algorithme qui calcule la valeur moyenne des éléments de T.

# somme_tableau(t: tableau d'entiers)
# pour element x dans le tableau T faire
# somme <- 
# somme <- somme + x
# Fin Pour

# moyenne <- somme / taille(T)
# retourne moyenne

tableau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # tableau de données en entier

def somme_tableau(T):# fonction nommée somme_tableau
    somme = 0 # initialisation de la variable

    for x in T:
        somme += x # valeur x dans la variable somme
        return somme
    
    def moyenne_tableau(T):# moyenne des éléments du tableau
        somme = 0
        for x in T:
            somme += x
            moyenne = somme / len(T) # calcule moyenne en divisant la somme par la longueur du tableau T
            return moyenne # retourne les éléments du tableau
        
        resultat_somme = somme_tableau(tableau)
        resultat_moyenne = moyenne_tableau(tableau)

        print("Somme des éléments du tableau:", resultat_somme)
        print("Moyenne des éléments du tableau:", resultat_moyenne)