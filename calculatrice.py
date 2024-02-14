def addition(a :float, b :float) -> float:
    return a + b

def soustraction(a, b)-> float:
    return a - b

def calculatrice() -> None:
    while True:
        print("Faites votre choix")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Quitter")

        choix = input("Entrez votre choix (1-3)")

        if choix == '3':
            break

        if choix in ('1', '2'):
            a = float(input("Entrez le premier nombre"))
            b = float(input("Entrez le deuxieme nombre"))
            if choix == '1':
                print("Resultat", addition(a, b))
            elif choix == '2':
                print("Resultat", soustraction(a, b))
        else:
            print("Choix non valide")


