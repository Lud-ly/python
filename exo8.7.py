twoDim=[[10],[10]]
i=0
j=0
pion_x=0
pion_y=0
new_x=0
new_y=0

for x in range (10):
  for y in range (10):
    twoDim=[x][y]


def testMove(move,pion_x,pion_y):
  correct = True
  if(move== 0):
    new_x=pion_x -1
    new_y=pion_y-1

  elif(move== 1):
    new_x=pion_x -1
    new_y=pion_y+1

  elif(move== 2):
    new_x=pion_x +1
    new_y=pion_y-1

  else:
    new_x=pion_x +1
    new_y=pion_y+1  

  if (new_x <0 or new_x>9):
    correct = False
  elif (new_y <0 or new_y>9):
    correct = False

  if(correct):
    twoDim[pion_x][pion_y] =0
    twoDim[new_x][new_y]=1
    """displayBoard()""" 
  else:
    print("mouvement impossible")  

def checkLine(input):
  correct= False
  resultat =0
  while(correct==True):
    resultat=(input("Sur quelle ligne se trouve votre pion?"))
    if (resultat)>0 and resultat<=10:
      correct=True
    return resultat

def checkCol(input):
  correct= False
  resultat =0
  while(correct==True):
    resultat=(input("Sur quelle colonne se trouve votre pion?"))
    if (resultat)>0 and resultat<=10:
      correct=True
    return resultat

def checkMove(input):
  correct= False
  resultat =0
  while(correct==True):
    resultat=(input("quel mouvement voulez-vous faire? 0.1,2 ou 3 : "))
    if (resultat)>=0 and resultat<=3:
      correct=True
    return resultat

def displayBoard():
  print("[")
  for x in range (10):
    print("[")
    for y in range (10):
      print(twoDim[x][y])
      if(y!=9):
        print(",")
    print("] /n") 
  print("] /n")         
"""ALGO
Variables i, j , posi, posj, i2, j2 en Entier
Variables Correct, MoveOK en Booléen
Tableau Damier(7, 7) en Booléen
Tableau Mouv(3, 1) en Entier
Debut
Choix 0 : pion en haut à droite
Mouv(0, 0) ← -1
Mouv(0, 1) ← -1
Choix 1 : pion en haut à droite
Mouv(1, 0) ← -1
Mouv(1, 1) ← 1
Choix 2 : pion en bas à gauche
Mouv(2, 0) ← 1
Mouv(2, 1) ← -1
Choix 3 : pion en bas à droite
Mouv(3, 0) ← 1
Mouv(3, 1) ← 1
Initialisation du damier; le pion n’est pour le moment nulle part
Pour i ← 0 à 7
  Pour j ← 0 à 7
    Damier(i, j) ← Faux
  j suivant
i suivant
Saisie de la coordonnée en i ("posi") avec contrôle de saisie
Correct ← Faux
TantQue Non Correct
  Ecrire "Entrez la ligne de votre pion: "
  Lire posi
  Si posi >= 0 et posi <= 7 Alors
    Correct ← vrai
  Finsi
Fintantque
Saisie de la coordonnée en j ("posj") avec contrôle de saisie
Correct ← Faux
TantQue Non Correct
  Ecrire "Entrez la colonne de votre pion: "
  Lire posj
    Si posj >= 0 et posj <= 7 Alors
      Correct ← Vrai
    Finsi
Fintantque
Positionnement du pion sur le damier virtuel.
Damier(posi, posj) ← Vrai
Saisie du déplacement, avec contrôle
Ecrire "Quel déplacement ?"
Ecrire " - 0: en haut à gauche"
Ecrire " - 1: en haut à droite"
Ecrire " - 2: en bas à gauche"
Ecrire " - 3: en bas à droite"
Correct ← Faux
TantQue Non Correct
  Lire Dep
  Si Dep >= 0 et Dep <= 3 Alors
    Correct ← Vrai
  FinSi
FinTantQue
i2 et j2 sont les futures coordonnées du pion. La variable booléenne MoveOK vérifie la validité de ce futur emplacement
i2 ← posi + Mouv(Dep, 0)
j2 ← posj + Mouv(Dep, 1)
MoveOK ← i2 >= 0 et i2 <= 7 et j2 >= 0 et j2 <= 7
Cas où le déplacement est valide
Si MoveOK Alors
  Damier(posi, posj) ← Faux
  Damier(i2, j2) ← Vrai
Affichage du nouveau damier
  Pour i ← 0 à 7
    Pour j ← 0 à 7
      Si Damier(i, j) Alors
        Ecrire " O ";
      Sinon
        Ecrire " X ";
      FinSi
    j suivant
    Ecrire ""
  i suivant
Sinon
Cas où le déplacement n’est pas valide
  Ecrire "Mouvement impossible"
FinSi
Fin
"""

  

