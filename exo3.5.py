# exercice 3.5
"""ALGO
Variables a, b en Entier
Début
Ecrire "Entrez deux nombres : "
Lire a, b
Si (a = 0 OU b = 0)  (a > 0 ou b < 0) et (a < 0 ou b > 0) Alors
  Ecrire "Le produit est nul"
SinonSi (a > 0 ou b > 0) Alors
  Ecrire "Le produit est positif"
SinonSi (a < 0 ou b < 0)  
  Ecrire "Le produit est négatif"
Finsi
Fin"""
def exo():
  a = int(input("Entrez le premier nombre"))
  b = int(input("Entrez le second nombre"))
  if a == 0 or b == 0  :
      print("le produit est null")
  elif a > 0 and b > 0:
      print("le produit est positif")
  elif a < 0 and b < 0:
      print("le produit est negatif")
exo()




"""JAVA
public class Main
{
    public static void main(String[] args) 
    {
       int nbr = 5;
       if(nbr > 0)
         System.out.println(nbr+" est un nombre positif");
       else if(nbr < 0)
         System.out.println(nbr+" est un nombre négatif");
       else   
         System.out.println(nbr+" n'est ni positif ni négatif");
    }
}
 """