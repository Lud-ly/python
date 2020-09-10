#excercice 5.2b
import random
r = random.randint(1, 100)
print(r)
coups = 0
nombreEntre = int(input("saisir un nombre"))
while nombreEntre < r and nombreEntre > r:
      nombreEntre = int(input("resaisir un nombre"))  
      coups += 1
if nombreEntre < r:  
      coups += 1
      print("C'est Plus!")
      nombreEntre = int(input("resaisir un nombre"))
if nombreEntre > r:
      coups += 1
      print("C'est Moins!")
      nombreEntre = int(input("resaisir un nombre"))  
if nombreEntre == r:
      print("C'est gagné! vous avez effectué",coups,"coups")