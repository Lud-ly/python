"""ALGO
Variable Bla, Cod, Alpha en Caractère
Variables i, Pos, Décal en Entier
Début
Ecrire "Entrez l’alphabet clé : "
Lire Clé
Ecrire "Entrez la phrase à coder : "
Lire Bla
Alpha ← "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Cod ← ""
Pour i ← 1 à Len(Bla)
  Let ← Mid(Bla, i, 1)
  Pos ← Trouve(Alpha, Let)
  Cod ← Cod & Mid(Clé, Pos, 1)
i Suivant
Bla ← Cod
Ecrire "La phrase codée est : ", Bla
Fin"""