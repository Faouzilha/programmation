# Ecrire un algorithme en pseudo-code qui lit le prix HT d’un article, le nombre d’articles et 
# le taux de TVA, et qui fournit le prix total TTC correspondant. 
# Faire en sorte que des libellés apparaissent clairement.

# Variables : nombre, pht, ttva, pttc
# Debut

    # Ecrire "Entrez le prix HT"
    # Lire (prix HT)
    # Ecrire "Entrez le nombre d'articles:"
    # Lire (nombre)
    # Ecrire "Entrez le taux de TVA"
    # Lire (TVA)

    # pttc<- nombre * pht(1 + TVA)
    # Ecrire "Le prix TTC est:", PTTC

# Fin


nombre = 0
pht = 0.0
ttva = 0.0
pttc = 0.0

print("Entrez le prix hors taxes :") # valeurs
pht = float(input())  # Conversion à virgule

print("Entrez le nombre d’articles :")
nombre = int(input())  # Conversion nombre entier

print("Entrez le taux de TVA :")
ttva = float(input()) / 100  # Conversion à virgule

pttc = nombre * pht * (1 + ttva) # Calcul ttc


print("Le prix toutes taxes est :", pttc) # Résultat