<<<<<<< HEAD
"""ALGO
Variables montant_verse, price, payer, Reste, bil10E, bil5E En Entier
Debut
price ← 100
montant_verse ← 0
TantQue montant_verse = 0
  Ecrire "Ecrire le montant:"
  Lire montant
  price = price - montant_verse
Fin TantQue
Ecrire ""vous nous devez :",price,"€""
Ecrire "payer somme due :"
Lire payer
reste ← payer - price
bil10E ← 0
TantQue Reste >= 10
  bil10E ← bil10E + 1
  Reste ← Reste – 10
Fin TantQue
bil5E ← 0
Si Reste >= 5
  bil5E ← 1
  Reste ← Reste – 5
FinSi
Ecrire "Retour de la monnaie :"
Ecrire bil10E,"Billets de 10 E" 
Ecrire  bil5E,"Billets de  5"
Ecrire  reste, "Pièces de 1"
Fin"""
price = 100
montant_verse = 0
while price == 0:
  montant_verse=(input("Ecrire le versement:"))
  price = price - montant_verse
print("vous nous devez :",price,"€")  
payer= float(input("payer la somme dûe :")) 
reste = payer - price
bil10E = 0
while reste >= 10:
  bil10E = bil10E + 1 
  reste = reste - 10
bil5E = 0    
if reste >= 5:
  bil5E = 1 
  reste = reste - 5
print("Retour de la monnaie :") 
print(bil10E,"billet de 10") 
print(bil5E,"billet de 5") 
print(reste,"piece de 1€") 
=======
"""Variables E, somdue, M, Reste, Nb10E, Nb5E En Entier
Debut
E ← 1
somdue ← 0
TantQue E <> 0
  Ecrire "Entrez le montant : "
  Lire E
  somdue ← somdue + E
FinTantQue
Ecrire "Vous devez :", somdue, " euros"
Ecrire "Montant versé :"
Lire M
Reste ← M - somdue
Nb10E ← 0
TantQue Reste >= 10
  Nb10E ← Nb10E + 1
  Reste ← Reste – 10
FinTantQue
Nb5E ← 0
Si Reste >= 5
  Nb5E ← 1
  Reste ← Reste – 5
FinSi
Ecrire "Rendu de la monnaie :"
Ecrire "Billets de 10 E : ", Nb10E
Ecrire "Billets de  5 E : ", Nb5E
Ecrire "Pièces de 1 E : ", reste
Fin"""
e = 1 
somdue = 0 

while e < 10: 
print("entrez le montant")
somdue == somdue + e
print("vous devez" , somdue , "euros")
>>>>>>> 47aae0ba4576358d7f5739f4564c75d7fb2fad8f
