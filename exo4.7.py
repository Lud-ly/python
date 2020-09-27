# excercice 4.7

age = int(input("Saisir votre age : "))
perm = int(input("Votre nombre d'années permis : "))
acc = int(input("Le nombre d'accidents : "))
assur = int(input("Le nombre d'années d'assurance : "))
c1 = age >= 25
c2 = perm >= 2
c3 = assur > 5
situ = ""

if c1 ==False and c2 == False:
    if acc == 0:
        situ=("rouge")
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
print("votre situation",situ)  
if c3 ==True:
   if situ == "rouge":
       situ = "orange"
   elif  situ == "orange":
       situ = "vert"
   elif situ == "vert":
       situ = "bleu"

print("votre situation apres ancienneté",situ) 

