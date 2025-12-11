def saisir_nombre():
    """Demande un nombre entier à l'utilisateur et vérifie la saisie."""
    while True:
        valeur = input("Saisissez un nombre entier: ")
        if valeur.lstrip("-").isdigit():   # gère aussi les nombres négatifs
            return int(valeur)
        print("Erreur ! Veuillez saisir un nombre entier.")


def est_pair(nombre):
    """Retourne True si le nombre est pair, sinon False."""
    return nombre % 2 == 0


def main():
    nombre = saisir_nombre()

    if est_pair(nombre):
        print("Le nombre est pair.")
    else:
        print("Le nombre est impair.")

    print("Fin du programme.")


# Lancement du programme
main()
