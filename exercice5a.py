def ajouter_tache():
    description = input("Description de la tâche : ")
    statut = input("Statut (à faire / en cours / terminé) : ")

    print("\nTâche ajoutée :")
    print(" -", description)
    print(" -", statut)

# Appel de la fonction
ajouter_tache()
a=ajouter_tache()
print(a)
