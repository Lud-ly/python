import random

jouer = input ("Lancer les dés? True/False : ")

FaceDe=("",
        """ _____ 
|     |
|  o  |
|     |
|_____|""",
        """ _____ 
| o   |
|     |
|   o |
|_____|""",
""" _____ 
| o   |
|  o  |
|   o |
|_____|""",""" _____ 
| o o |
|     |
| o o |
|_____|""",""" _____ 
| o o |
|  o  |
| o o |
|_____|""",""" _____ 
| o o |
| o o |
| o o |
|_____|"""        )

while (jouer): 
   
   #3 tirages
   tirage=[]
   tirage.append(random.randrange(1,6))  #entre 1 et 6
   tirage.append(random.randrange(0,5)+1) #( entre 0 et 5 ) +1 => entre 1 et 6
   tirage.append(random.randrange(5)+1)  # idem ci-dessus toujours entre 1 et 6

   #affichage du tirage et des points obtenus
   points=0
   i= 0
   while(i<=2):
      print (FaceDe[tirage[i]],tirage[i])
      points= points+tirage[i]
      i=i+1
   print ("Vous avez gagné "+str(points)+ " points à ce lancer")
   rep = input ("rejouer? (o/n)")
   if (rep !="o" and rep !="O"):
      jouer=False
"""from random import randint

S=0
N=int(input("nombre de lancers : "))

for i in range(1,N+1):
  jeu=randint(1,6)
  if jeu ==6:
       S=+1
print("le nombre de glup sur",N,"lancers est de : ",S)       

S←0
Saisir N
Pour I allant de 1 à N Faire
 JEU ← nbre entier
aléatoire entre 1 et 6
 Si Jeu = 6 alors faire
 S←S+1
 FinSi
FinPour
Afficher S
"""

