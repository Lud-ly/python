Nbposi = 0
Nbnega = 0
numbers=0
for num in  range (5):
  numbers = (int(input("Entrez le nombre de valeurs :")))
  if numbers >=0:
    Nbposi+=1
  else:
    Nbnega+=1
print("il y a ",Nbposi,"valeur positive")           
print("il y a ",Nbnega,"valeur negative")           