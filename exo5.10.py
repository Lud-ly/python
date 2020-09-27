price = 100
montant_verse = 0
bil10E = 0
bil5E = 0  
while price == 0:
  montant_verse=(input("Ecrire le versement:"))
  price = price - montant_verse
print("vous nous devez :",price,"€")  
payer= float(input("payer la somme dûe :")) 
reste = payer - price

while reste >= 10:
  bil10E = bil10E + 1 
  reste = reste - 10
  
if reste >= 5:
  bil5E = 1 
  reste = reste - 5
print("Retour de la monnaie :") 
print(bil10E,"billet de 10") 
print(bil5E,"billet de 5") 
print(reste,"piece de 1€") 
