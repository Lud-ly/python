"""ALGO
Variables Nb, Nbposi, Nbnega en Numérique
Tableau T() en Numérique
Debut
Ecrire "Entrez le nombre de valeurs :"
Lire Nb
Redim T(Nb-1)
Nbposi ← 0
Nbnega ← 0
Pour i ← 0 à Nb - 1
  Ecrire "Entrez le nombre n° ", i + 1
  Lire T(i)
  Si T(i) > 0 alors
    Nbposi ← Nbposi + 1
  Sinon
    Nbnega ← Nbnega + 1
  Finsi
Ecrire "Nombre de valeurs positives : ", Nbposi
Ecrire "Nombre de valeurs négatives : ", Nbnega
Fin"""
T = (0)
Nb = input("Entrez le nombre de valeurs :")
Redim T (Nb-1)
Nbposi = 0
Nbnega = 0
for i in range(1,Nb-1):
    T = int(input("Entrez le nombre n° ", i + 1))
    if T(i) > 0:
        Nbposi = Nbposi + 1
    else:
        Nbnega = Nbnega + 1    
print("Nombre de valeurs positives : ", Nbposi)        
print("Nombre de valeurs negatives : ", Nbnega)        