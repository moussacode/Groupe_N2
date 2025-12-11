# Exercice 1 – Afficher la table de multiplication d’un nombre (1 à 10)

n = int(input("Entrez un nombre : "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
