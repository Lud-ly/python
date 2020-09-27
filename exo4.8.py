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









