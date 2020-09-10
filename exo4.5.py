"""Variable sex en Caractère
Variable age en Numérique
Variables C1, C2 en Booléen
Début
Ecrire "Entrez le sexe (M/F) : "
Lire sex
Ecrire "Entrez l’âge: "
Lire age
C1 ← sex = "M" ET age > 20
C2 ← sex = "F" ET (age > 18 ET age < 35)
Si C1 ou C2 Alors
  Ecrire "Imposable"
Sinon
  Ecrire "Non Imposable"
FinSi
Fin"""
sex = ""
sex = str(input("entrez le sexe H/F"))
age = int(input("ENTREZ VOTRE AGE"))
c1 = sex = "H" and age > 20
c2 = sex = "F" and (age > 18 and age < 35)
if c1 and c2:
    print("imposable")
else:
    print("non-imposable")    