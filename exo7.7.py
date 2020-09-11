"""ALGO
i <- 1
j <- 1
k <- 1
 
TANT QUE i <= n et j <= m FAIRE
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
T1 =[]
T2 =[]
T=[]
m =0
t=[]
n=0
i = 0
j = 0
k = 0
while i <= n and j <= m:
    if T1[i] < T2[j]:
        t[k]= T1[i]
        k =k + 1
        i =i+1
    else:
        T[k] <- T2[j]
        k <- k+1
        j <- j+1
      
while i <= n :
    T[k] <- T1[i]
    k <- k+1
    i <- i+1
while j <= m :
    T[k] <- T2[j]
    k <- k+1
    j <- j+1
    
    """autre tentative
    val=0
for i in (0,1):
    for j in (0,2):
        X=(i,j) = val
        val = val +1
for i in (0,1):
    for j in (0,2):
        print(X(i,j))
    """