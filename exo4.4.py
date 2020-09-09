"""excercice4.4
Variables n, p en Numérique
Début
Ecrire "Nombre de photocopies : "
Lire n
Si n <= 10 Alors
  p ← n * 0,1
SinonSi n <= 30 Alors
  p ← 10 * 0,1 + (n – 10) * 0,09
Sinon
  p ← 10 * 0,1 + 20 * 0,09 + (n – 30) * 0,08
FinSi
Ecrire "Le prix total est: ", p
Fin"""
n = 0
p = 0
n = int(input("Nombre de photocopies :"))
if n <= 10 :
    p = n * 0.1 
    print("le prix total est de", p)  
elif n <= 30 :
    p = 10 * 0.1 + (n - 10) * 0.09          
    print("le prix total est de", p)
else:
    p = 10 * 0.1 + 20 * 0.09 + (n - 30) * 0.08
    print("le prix total est de", p)  