# excercice 3.6
"""ALGO
Variable age en Entier
Début
Ecrire "Entrez l’âge de l’enfant : "
Lire age
Si age >= 12 Alors
  Ecrire "Catégorie Cadet"
SinonSi age >= 10 Alors
  Ecrire "Catégorie Minime"
SinonSi age >= 8 Alors
  Ecrire "Catégorie Pupille"
SinonSi age >= 6 Alors
  Ecrire "Catégorie Poussin"
Finsi
Fin"""
age = int(input("saisir votre age"))
if age >= 12:
    print("category cadet")
elif age >= 10:
    print("category minime")
elif age >= 8:
    print("category pupille")
elif age >= 6:
    print("category poussin")
    