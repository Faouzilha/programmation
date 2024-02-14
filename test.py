
# # Déclaration des variables avec leurs types
# note1: float
# note2: float
# note3: float
# moyenne: float
# mention: str

# # Saisie des notes en tant que nombres réels
# note1 = float(input("Entrez la première note : "))
# note2 = float(input("Entrez la deuxième note : "))
# note3 = float(input("Entrez la troisième note : "))

# # Calcul de la moyenne
# moyenne = (note1 + note2 + note3) / 3

# # Attribution de la mention en fonction de la moyenne
# if moyenne < 10:
#     mention = "Recalé"
# elif moyenne <= 12:
#     mention = "Passable"
# elif moyenne <= 14:
#     mention = "Assez bien"
# elif moyenne <= 16:
#     mention = "Bien"
# else:
#     mention = "Très bien"

# # Affichage du résultat
# print("Votre moyenne est de", moyenne, "et vous avez la mention :", mention)




# Variables
som = 0
i = 0

# Première itération (i = 1, som = 1)
# Deuxieme itération (i = 2, som = 3)
# Troisieme itération (i = 3, som = 6)
# Quatrieme itération (i = 4, som = 10)
# Boucle tant que
# while som <= 100:
#     i += 1
#     som += i
#     print(i, " Iteration, somme = ", som)

# # Affichage du résultat
# print("La valeur cherchée est N =", i)
# print("La somme est N =", som)


# # python
# N = 0
# i = 0

# N = int(input("Entrez un nombre : "))

# print("Les 10 nombres suivants sont : ")
# while i < 10:
#     i = i + 1
#     print(N + i)



# python - Solution 1

# N = int(input("Entrez un nombre entier positif : "))
# i = 0

# print("Les 10 nombres suivants sont : ")
# while i <= N:
#     print(i)
#     i += 2

# # python - Solution 2

# N = int(input("Entrez un nombre entier positif : "))
# i = 0

# print("Tous les nombres pairs suivants sont : ")
# while i <= N:
#     if i % 2 == 0:  
#         print(i)
#     i = i + 1

# while True:
#     nombre = int(input("Entrez un nombre entre 10 et 20 : "))

#     if nombre < 10:
#         print("Plus grand !")

#     elif nombre > 20:
#         print("Plus petit !")

#     else:
#         break
#     print("Vous avez saisi un nombre valide entre 10 et 20. Merci !")


# Calcul de x à la puissance n où x est un réel non nul et n un entier positif ou null

# Pseudo-code

# Variables x, puiss : réel
# n, i : entier
# Debut
#   Ecrire (" Entrez la valeur de x ")
#   Lire (x)
#   Ecrire (" Entrez la valeur de n ")
#   Lire (n)
# La variable puiss est initialement definit a 1 , car elle est mulitpliee par la valeur de x "
# cela permet d'accumuler le resultat de x par lui-meme n fois, simulant la pussance de x^n
#   puiss ← 1
#   Pour i allant de 1 à n
#       puiss ← puiss * x
#   FinPour
#   Ecrire (x, " à la puissance ", n, " est égal à ", puiss)
# Fin

# python
# x, puiss = 1.0, 1.0  # Initialisation de x et puiss à 1.0 pour les traiter comme des réels
# n, i = 0, 0  # Initialisation de n et i à 0

# # Demander à l'utilisateur la valeur de x
# x = float(input("Entrez la valeur de x : "))

# # Demander à l'utilisateur la valeur de n
# n = int(input("Entrez la valeur de n : "))

# # Calculer x à la puissance n
# for i in range(1, n + 1):
#     puiss *= x

# # Afficher le résultat
# print(x, " à la puissance ", n, " est égal à ", puiss)

# # Autres solutions
# # Methode pow(...) qui retourne la puissance de x par n
# puiss2 = pow(x, n);
# print(x, " à la puissance ", n, " est égal à ", puiss2)
# # Operateur ** pour la puissance
# puiss3 = x ** n;
# print(x, " à la puissance ", n, " est égal à ", puiss3)


# var N, i en Entier
# Debut
# Ecrire ("Entrez un nombre:")
# Lire(N)
# Pour i de 1 à 10
# Ecrire(N+i)
# Fin pour
# Fin



# Initialise la variable N à zéro.  déclare avant de l'utilisation
# N = 0
# #  Demande utilisateur d'entrer un nombre à partir de la console. La fonction input prend l'entrée de l'utilisateur 
# # sous forme de chaîne de caractères, et int() convertit cette chaîne en un entier. 
# # La valeur entrée par l'utilisateur est ensuite assignée à la variable N.
# N = int(input("Entrez un nombre : "))
# print("Les 10 nombres suivants sont : ")
# # boucle for qui itère sur les valeurs de i de 1 à 10 (inclus). La fonction range(1, 11) génère une séquence d'entiers commençant 
# # à 1 et se terminant à 10
# for i in range(1, 11):
#     print(N + i)
#     # À chaque itération de la boucle, affiche la valeur de N + i. Cela imprime les 10 nombres suivants à partir du nombre entré par l'utilisateur.

# import random

# nombreSecret = random.randint(1, 100)
# tentative = 0
# print("Devinez le nombre entre 1 et 100")

# while True:
#     proposition = int(input("Entrez la proposition : "))  
#     tentative += 1

#     if proposition < nombreSecret:
#         print("Trop petit !")
#     elif proposition > nombreSecret:
#         print("Trop grand !")
#     else:
#         print("Gagné, nombre deviné !")

#         break

    
# print("Nombre de tentatives :", tentative)

# max_nombre = 0  # Initialisation avec une valeur très petite

# for i in range(1, 21): # code s'executera 20 fois
#     print("Entrez le nombre numéro ", i,":" )
#     nombre = int(input())
    
#     if nombre > max_nombre:
#         max_nombre = nombre

# print("Le plus grand nombre parmi les 20 saisis est : ", max_nombre)


def somme_des_carres(n):
    somme = 0
    for i in range(1, n + 1):
        somme += i ** 2
    return somme

n = int(input("Veuillez entrer un nombre entier positif n : "))

resultat = somme_des_carres(n)

print("La somme des carrés de 1 à n  est : ", resultat)
