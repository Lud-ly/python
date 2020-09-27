import random


tableau=[]
tab_lenght = 5
tableau = [tab_lenght]
valeur = 0
j = 0
i=0

for i in range(tab_lenght):
    valeur=(int(input("veuillez saisir des valeurs:"))) 
    

#for j in tableau:
    #print(tableau[j]+",")    


def tri_insertion(tableau):
    for i in  range(len(tableau)):
        valeur = tableau[i]
        j = i
        while(j>0 and tableau[j-1]>valeur):
            tableau[j] =tableau[j-1]
            j=j-1
        tableau[j] = valeur


tri_insertion(tableau)
for valeur in tableau:
    print("la",tableau[j])

"""def tri_insertion(liste):
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
    liste.append(random.randint(0,100))
    liste_triee = tri_insertion(liste)

                      
print("list non trié",liste)
print("liste croissante",liste_triee)"""

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
