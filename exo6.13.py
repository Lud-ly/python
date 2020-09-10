"""ALGO
Variables Nb, Posmaxi en Numérique
Tableau T() en Numérique
Ecrire "Entrez le nombre de valeurs :"
Lire Nb
Redim T(Nb-1)
Pour i ← 0 à Nb - 1
  Ecrire "Entrez le nombre n° ", i + 1
  Lire T(i)
i Suivant
Posmaxi ← 0
Pour i ← 0 à Nb - 1
  Si T(i) > T(Posmaxi) alors
    Posmaxi ← i
  Finsi
i Suivant
Ecrire "Element le plus grand : ", T(Posmaxi)
Ecrire "Position de cet élément : ", Posmaxi
Fin"""