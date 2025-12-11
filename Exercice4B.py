def est_palindrome(mot):
    
    mot = mot.lower()       # pour ignorer majuscules/minuscules
    mot = mot.replace(" ", "")  # pour ignorer les espaces
    return mot == mot[::-1]

def saisir_mot():
    """Demande un mot à l’utilisateur et le retourne."""
    return input("Saisissez un mot : ")

def main():
    mot = saisir_mot()
    
    if est_palindrome(mot):
        print("Le mot est un palindrome.")
    else:
        print("Le mot n'est pas un palindrome.")
    
    print("Fin du programme.")


# Lancement
main()
