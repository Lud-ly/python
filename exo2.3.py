print("hello Python")
"""ALGO
Variables nbr, prixht, taux, result en Numérique
Début
Ecrire "Entrez le prix hors taxes :"
Lire prixht
Ecrire "Entrez le nombre d’articles :"
Lire nbr
Ecrire "Entrez le taux de TVA :"
Lire taux
result ← nbr * prixht * (1 + taux/100)
Ecrire "Le prix TTC est : ", result
Fin"""
# exercice 2.3
prixht = int(input("Entrez le prix du produit ht"))
nbr = int(input("Entrez le nombre d'articles"))
taux = float(input("Entrez le taux de TVA"))
result = (prixht * nbr) * (1 + taux/100)
print("le prix TTC est de:", result, "€")
