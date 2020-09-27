print("hello Python")
# exercice 2.3
prixht = int(input("Entrez le prix du produit ht"))
nbr = int(input("Entrez le nombre d'articles"))
taux = float(input("Entrez le taux de TVA"))
result = (prixht * nbr) * (1 + taux/100)
print("le prix TTC est de:", result, "€")
