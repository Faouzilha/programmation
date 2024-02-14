# Ecrire un algorithme qui lit deux nombre A, B et affiche le plus grand

# Variables A, B : entier

    # Ecrire "Entrez le nb A"
    # Lire (A)

    # Ecrire "Entrez le nb B"
    # Lire (B)

# si A > B Alors
    # Ecrire "Le plus grand nb est A:", A

# sinon si B > A Alors
    # Ecrire "Le plus grand nb est B:, B

# sinon
    # Ecrire "Les 2 nb sont égaux"
# finSi


A = float(input("Entrez le nombre A : ")) # utilisateur entre deux nombres
B = float(input("Entrez le nombre B : "))

# Compare  et affiche le résultat
if A > B:
    print("Le plus grand nombre est A :", A)
elif B > A:
    print("Le plus grand nombre est B :", B)
else:
    print("Les deux nombres sont égaux.")
