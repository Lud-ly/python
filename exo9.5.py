"""ALGO
Variable Bla en Caractère
Variables Nb, i, j en Entier
Début
Ecrire "Entrez une phrase : "
Lire Bla
Ecrire "Entrez le rang du caractère à supprimer : "
Lire Nb
L ← Len(Bla)
Bla ←  bla[:nb] + bla[nb+1:]

Ecrire "La nouvelle phrase est : ", Bla
Fin"""
bla = input("Entrez la phrase : ")
nb = int(input("Entrez le rang du caractère à supprimer : "))
l = len(bla)

bla = bla[:nb] + bla[nb+1:]

print("la nouvelle phrase est :",bla)
bla2 = input("Entrez la phrase : ")
bla2 = bla2.replace(bla,bla[nb])
print(bla2+bla)