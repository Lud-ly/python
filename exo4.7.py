# excercice 4.7
situ = "initial"

age = int(input("saisir votre age"))
perm = int(input("nombre d'années permis"))
acc = int(input("nombre d'accidents"))
assur = int(input("nombre d'années d'assurance"))
age >= 25
perm >= 2
assur > 5

if age<=25 and perm<=2:
    if acc == 0:
       print("rouge")
    else:
        print("refusé")

elif (age<=25 and perm)or(age and perm>=2):
    if acc ==0:
         print("orange")
    elif acc ==1:
            print("rouge")
    else:
             print("refusé")

if acc ==0:
         print("vert")
elif acc == 1: 
    print("orange")
elif acc == 2:
    print("rouge")
else:
    print("refusé")


if assur >= 5:
    print("orange")
elif  situ == "orange":
    print("vert")
elif situ == "vert":
    print("bleu") 
print("votre situation",situ)  