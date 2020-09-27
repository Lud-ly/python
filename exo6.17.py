import random

def tri_insertion(liste):
    myList = list(liste) 
    longeurList = len(myList)
    for n in range(1,longeurList):
        cle = myList[n]
        j = n-1
        while j>=0 and myList[j] > cle:
            myList[j+1] = myList[j] # decalage
            j = j-1
        myList[j+1] = cle
    return myList
    
liste = []
for k in range(10):
    liste.append(random.randint(0,100))
    liste_triee = tri_insertion(liste)
    print("insertion new nbr->",liste_triee)
                      

print("liste triée par insertion",liste_triee)


