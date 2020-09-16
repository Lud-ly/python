"""Variables Bla, Cod, Alpha en Caractère
Variables i, Pos en Entier
Début
Ecrire "Entrez la phrase à coder : "
Lire Bla
Alpha ← "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Cod ← ""
Pour i ← 1 à Len(Bla)
  Let ← Mid(Bla, i, 1) 
  Si Let <> "Z" Alors
    Pos ← Trouve(Alpha, Let)
    Cod ← Cod & Mid(Alpha, Pos + 1, 1) 
  Sinon
    Cod ← Cod & "A" 
  FinSi
i Suivant
Bla ← Cod
Ecrire "La phrase codée est : ", Bla
Fin"""
i = 0
pos = 0
bla = input("Entrez la phrase à coder :")
cod = ""