# excercice 4.7
"""ALGO
Variables age, perm, acc, assur en Numérique
Variables C1, C2, C3 en Booléen
Variable situ en Caractère
Début
Ecrire "Entrez l’âge: "
Lire age
Ecrire "Entrez le nombre d'années de permis: "
Lire perm
Ecrire "Entrez le nombre d'accidents: "
Lire acc
Ecrire "Entrez le nombre d'années d'assurance: "
Lire assur
C1 ← age >= 25
C2 ← perm >= 2
C3 ← assur > 5
Si Non(C1) et Non(C2) Alors
  Si acc = 0 Alors
    situ ← "Rouge"
  Sinon
    situ ← "Refusé"
  FinSi
Sinonsi ((Non(C1) et C2) ou (C1 et Non(C2)) Alors
  Si acc = 0 Alors
    situ ← "Orange"
  SinonSi acc = 1 Alors
    situ ← "Rouge"
  Sinon
    situ ← "Refusé"
  FinSi
Sinon
  Si acc = 0 Alors
    situ ← "Vert"
  SinonSi acc = 1 Alors
    situ ← "Orange"
  SinonSi acc = 2 Alors
    situ ← "Rouge"
  Sinon
    situ ← "Refusé"
  FinSi
FinSi
Si C3 Alors
  Si situ = "Rouge" Alors
    situ ← "Orange"
  SinonSi situ = "Orange" Alors
    situ ← "Vert"
  SinonSi situ = "Vert" Alors
    situ ← "Bleu"
  FinSi
FinSi
Ecrire "Votre situation : ", situ
Fin"""
situ = ""

age = int(input("saisir votre age"))
perm = int(input("nombre d'années permis"))
acc = int(input("nombre d'accidents"))
assur = int(input("nombre d'années d'assurance"))
c1 = age >= 25
c2 = perm >= 2
c3 = assur > 5
if c1 ==False and c2 == False:
    if acc == 0:
       situ("rouge")
    else:
        situ=("refusé")
elif (c1 ==False and c2==True)or(c1==True and c2==False):
    if acc == 0:
         situ=("orange")
    elif acc == 1:
         situ=("rouge")
    else:
         situ=("refusé")
else:         
    if acc == 0:
         situ=("vert")
    elif acc == 1: 
         situ=("orange")
    elif acc == 2:
         situ=("rouge")
    else:
         situ=("refusé")
 
if c3 ==True:
   if situ == "rouge":
       situ = "orange"
   elif  situ == "orange":
       situ = "vert"
   elif situ == "vert":
       situ = "bleu"

print("votre situation",situ) 



