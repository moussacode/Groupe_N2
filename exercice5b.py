def calculer_somme(liste):
    somme = 0
    for nombre in liste:
        somme += nombre
    return somme

# Exemple d'utilisation
nombres = [2, 5, 7, 10]
resultat = calculer_somme(nombres)
print("La somme est :", resultat)
