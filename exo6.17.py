import random
def tri_insertion(liste):
    L = list(liste) 
    N = len(L)
    for n in range(1,N):
        cle = L[n]
        j = n-1
        while j>=0 and L[j] > cle:
            L[j+1] = L[j] # decalage
            j = j-1
        L[j+1] = cle
    return L
    
liste = []
for k in range(100):
    liste.append(random.randint(0,100))
liste_triee = tri_insertion(liste)

                      
print(liste)
print(liste_triee)
