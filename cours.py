print("hello Python")

#exercice 2.3
prixht = int(input("Ecrire le prix du produit"))
nbr = int(input("la quantité"))
taux = 1.20
result = (prixht * nbr) / taux
print("prix apres 20 de remise",result,"€")

#exercice 3.5
a = 25
b = 35
if a == 0 or b == 0:
  print("le produit est null")
if a > 0 and b > 0:
    print("le produit est positif")
if a < 0 and b < 0:
     print("le produit est negatif")
else:
    print("le produit ne peut pas etre evalué")

#excercice 3.6
age = int(input("saisir votre age"))
if age >= 12:
    print("category cadet")
elif age >=10:
    print("category minime")
elif age >=8:
    print("category pupille")
elif age >=6:
    print("category poussin")
#excercice 4.7
 