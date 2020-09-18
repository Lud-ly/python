 """ALGO
        taille en numerique de la longeur du tableau
        pour i =1 à < taille
        j=i-1
        tant que j>=0 et tab[j]>index
        tab[j+1] = tab[j]
        j--
        tab[j+1]=index
         int[] tab = {1, 12, 4, 5, 93, 21, 8, 11}
         ecrire tab avant insertion
         ecrire tab apres insertion
        """
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
for k in range(10):
    liste.append(random.randint(0,10))
    liste_triee = tri_insertion(liste)

                      
print("list non trié",liste)
print("liste croissante",liste_triee)
