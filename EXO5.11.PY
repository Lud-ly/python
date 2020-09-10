#premier exemple
"""ALGO
Variables N, P,  en Entier
Debut Ecrire "Entrez le nombre de chevaux partants : "
Lire N
Ecrire "Entrez le nombre de chevaux joués : "
Lire P
Crée facto
    si n ←0
    return 1
    sinon 
    FF =fact(n-1)
    F = n * FF
    return F 
X = fact(n)/ fact(n-p)
Y = fact(n)/fact(p) * (n-p)
Ecrire "Dans l’ordre, une chance sur ", X,"de gagner"
Ecrire "Dans le désordre, une sur ", Y,"de gagner"
Fin"""
n = int(input("Entrez le nombre de chevaux partants :")) 
p = int(input("Entrez le nombre de chevaux joués :")) 
def fact (n):
     if n == 0:
         return 1
     else:
       FF =fact(n-1)
       F = n * FF
       return F 
X = fact(n)/ fact(n-p)
Y = fact(n)/fact(p) * (n-p)
print("dans l'ordre : une chance sur", X,"de gagner")
print("dans le desordre : une chance sur", Y,"de gagner")

"""ALGO EXEMPLE 2
Variables N, P, i, A, B en Numérique
Debut
Ecrire "Entrez le nombre de chevaux partants : "
Lire N
Ecrire "Entrez le nombre de chevaux joués : "
Lire P
A ← 1
B ← 1
Pour i ← 1 à P
  A ← A * (i + N - P)
  B ← B * i
i Suivant
Ecrire "Dans l’ordre, une chance sur ", A
Ecrire "Dans le désordre, une chance sur ", A / B
Fin"""
n = int(input("Entrez le nombre de chevaux partants :")) 
p = int(input("Entrez le nombre de chevaux joués :"))
A = 1
B = 1
for i in range(1,p):
   A = A * (i + n -p)
   B = B * i
print("Dans l’ordre, une chance sur ", A)
print("Dans le desordre, une chance sur ", B)

