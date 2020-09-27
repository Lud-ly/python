from random import randint
from random import uniform
import random


for i in range(1):
  print("( 0 =< Glup =< 2) =>",uniform(0,2))

for i in range(1):
  print("(1,35 =< Glup =< 1,65) =>",uniform(1.35,1.45))
 
for i in range(1):
  print("(–1 =< Glup =< 1 =>)",uniform(-1,1))
tirage=[]
tirage.append(random.randrange(1,6))  #entre 1 et 6
print("dès 6faces =>",tirage)
 
for i in range(1):
  print("(–10,5 =< Glup =< +6,5)",uniform(-10.5,6.5))     

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
