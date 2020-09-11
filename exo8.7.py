"""ALGO
Variables i, j , posi, posj, i2, j2 en Entier
Variables Correct, MoveOK en Booléen
Tableau Damier(7, 7) en Booléen
Tableau Mouv(3, 1) en Entier
Debut
Choix 0 : pion en haut à droite
Mouv(0, 0) ← -1
Mouv(0, 1) ← -1
Choix 1 : pion en haut à droite
Mouv(1, 0) ← -1
Mouv(1, 1) ← 1
Choix 2 : pion en bas à gauche
Mouv(2, 0) ← 1
Mouv(2, 1) ← -1
Choix 3 : pion en bas à droite
Mouv(3, 0) ← 1
Mouv(3, 1) ← 1
Initialisation du damier; le pion n’est pour le moment nulle part
Pour i ← 0 à 7
  Pour j ← 0 à 7
    Damier(i, j) ← Faux
  j suivant
i suivant
Saisie de la coordonnée en i ("posi") avec contrôle de saisie
Correct ← Faux
TantQue Non Correct
  Ecrire "Entrez la ligne de votre pion: "
  Lire posi
  Si posi >= 0 et posi <= 7 Alors
    Correct ← vrai
  Finsi
Fintantque
Saisie de la coordonnée en j ("posj") avec contrôle de saisie
Correct ← Faux
TantQue Non Correct
  Ecrire "Entrez la colonne de votre pion: "
  Lire posj
    Si posj >= 0 et posj <= 7 Alors
      Correct ← Vrai
    Finsi
Fintantque
Positionnement du pion sur le damier virtuel.
Damier(posi, posj) ← Vrai
Saisie du déplacement, avec contrôle
Ecrire "Quel déplacement ?"
Ecrire " - 0: en haut à gauche"
Ecrire " - 1: en haut à droite"
Ecrire " - 2: en bas à gauche"
Ecrire " - 3: en bas à droite"
Correct ← Faux
TantQue Non Correct
  Lire Dep
  Si Dep >= 0 et Dep <= 3 Alors
    Correct ← Vrai
  FinSi
FinTantQue
i2 et j2 sont les futures coordonnées du pion. La variable booléenne MoveOK vérifie la validité de ce futur emplacement
i2 ← posi + Mouv(Dep, 0)
j2 ← posj + Mouv(Dep, 1)
MoveOK ← i2 >= 0 et i2 <= 7 et j2 >= 0 et j2 <= 7
Cas où le déplacement est valide
Si MoveOK Alors
  Damier(posi, posj) ← Faux
  Damier(i2, j2) ← Vrai
Affichage du nouveau damier
  Pour i ← 0 à 7
    Pour j ← 0 à 7
      Si Damier(i, j) Alors
        Ecrire " O ";
      Sinon
        Ecrire " X ";
      FinSi
    j suivant
    Ecrire ""
  i suivant
Sinon
Cas où le déplacement n’est pas valide
  Ecrire "Mouvement impossible"
FinSi
Fin
"""