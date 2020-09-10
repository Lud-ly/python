<<<<<<< HEAD
"""ALGO
Si M < 1 ou M > 12 Alors
  Ecrire "Date Invalide"
SinonSi M = 2 Alors
  Si A divisible par 400 Alors
=======
"""Si M < 1 ou M > 12 Alors
  Ecrire "Date Invalide"
SinonSi M = 2 Alors
  Si A dp 400 Alors
>>>>>>> 47aae0ba4576358d7f5739f4564c75d7fb2fad8f
    Si J < 1 ou J > 29 Alors
      Ecrire "Date Invalide"
    Sinon
      Ecrire "Date Valide"
    FinSi
<<<<<<< HEAD
  SinonSi A divisible par 100 Alors
=======
  SinonSi A dp 100 Alors
>>>>>>> 47aae0ba4576358d7f5739f4564c75d7fb2fad8f
    Si J < 1 ou J > 28 Alors
      Ecrire "Date Invalide"
    Sinon
      Ecrire "Date Valide"
    FinSi
<<<<<<< HEAD
  SinonSi A divisible par 4 Alors
    Si J < 1 ou J > 29 Alors
=======
  SinonSi A dp 4 Alors
    Si J < 1 ou J > 29Alors
>>>>>>> 47aae0ba4576358d7f5739f4564c75d7fb2fad8f
      Ecrire "Date Invalide"
    Sinon
      Ecrire "Date Valide"
    FinSi
  Sinon
    Si J < 1 ou J > 28 Alors
      Ecrire "Date Invalide"
    Sinon
      Ecrire "Date Valide"
    FinSi
  FinSi
SinonSi M = 4 ou M = 6 ou M = 9 ou M = 11 Alors
  Si J < 1 ou J > 30 Alors
    Ecrire "Date Invalide"
  Sinon
    Ecrire "Date Valide"
  FinSi
Sinon
  Si J < 1 ou J > 31 Alors
    Ecrire "Date Invalide"
  Sinon
    Ecrire "Date Valide"
  FinSi
<<<<<<< HEAD
FinSi"""

J = int(input("Entrez le numéro du jour"))
M = int(input("Entrez le numéro du mois"))
A = int(input("Entrez l'année"))

if M < 1 or M >12 :
  print("date invalide")
elif M == 2 :
  if A // 400 :
    if J < 1 or J > 29 :
      print("date invalide")
    else:
      print("date valide")
  elif A // 100 :
    if J < 1 or J > 28 :
      print("date invalide")
    else:
      print("date valide")
  elif A // 4 : 
    if J < 1 or J >29:
      print("date invalide")
    else:
      print("date valide")           
  else:
    if J < 1 or J > 28:
      print("date invalide")
    else:
      print("date valide")

elif M == 4 or M == 6 or M == 9 or M ==11:
  if J < 1 or J > 30:
    print("date invalide")
  else:
    print("date valide")        
else:
  if J <1 or J>31:
    print("date invalide")
  else:
    print("date valide")  









=======
FinSi"""
>>>>>>> 47aae0ba4576358d7f5739f4564c75d7fb2fad8f
