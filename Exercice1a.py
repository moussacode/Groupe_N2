# Exercice 1 – Afficher la table de multiplication d’un nombre (1 à 10)

n = int(input("Entrez un nombre : "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
# Exercice 2 – Échanger les valeurs de deux variables A et B

A = input("Entrez A : ")
B = input("Entrez B : ")

A, B = B, A

print("Après échange : A =", A, ", B =", B)
# Exercice 3 – Afficher les nombres pairs entre 1 et 50

for i in range(1, 51):
    if i % 2 == 0:
        print(i)
