"""ALGO
Variables Nb, Posmaxi en Numérique
Tableau T() en Numérique
Ecrire "Entrez le nombre de valeurs :"
Lire Nb
Redim T(Nb-1)
Pour i ← 0 à Nb - 1
  Ecrire "Entrez le nombre n° ", i + 1
  Lire T(i)
i Suivant
Posmaxi ← 0
Pour i ← 0 à Nb - 1
  Si T(i) > T(Posmaxi) alors
    Posmaxi ← i
  Finsi
i Suivant
Ecrire "Element le plus grand : ", T(Posmaxi)
Ecrire "Position de cet élément : ", Posmaxi
Fin"""
T = [0]
Nb = 0
Nb = int(input("Entrez un nombre determiné de valeurs :")) 
T.append
for i in Nb - 1:
  i = int(input("Entrez le nombre n° ", i + 1))
  i = T
Pomaxi = 0
for i in Nb - 1:
  if T > Pomaxi:
    Pomaxi = 1
print("Element le plus grand : ",T)
print ("Position de cet élément : ",Pomaxi)