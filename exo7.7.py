"""ALGO
i <- 1
j <- 1
k <- 1

TANT QUE T1[i] < T2[j] FAIRE
    SI T1[i] < T2[j] ALORS
        T[k] <- T1[i]
        k <- k+1
        i <- i+1
    SINON
        T[k] <- T2[j]
        k <- k+1
        j <- j+1
    FIN SI
FIN TANT QUE

TANT QUE i <= n FAIRE
    T[k] <- T1[i]
    k <- k+1
    i <- i+1
FIN TANT QUE

TANT QUE j <= m FAIRE
    T[k] <- T2[j]
    k <- k+1
    j <- j+1
FIN TANT QUE
"""

list1 = [15, 25, 35, 4]
list2 = [55, 65, 75, 8]
list1.sort()
list2.sort()
import itertools
list3 = list(itertools.chain(list1, list2))
list3.sort()
print(list3)