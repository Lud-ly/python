nb = 0
Nbmax = 0
y =0 
pos = 0
i=0
print("entrer 5 nombres ->")
for i in range(5):
  nb = int(input("Entrez les nombres  :"))
  if (nb >Nbmax):
    Nbmax = nb
    pos = y
    y = y+1
    

print("le nombre le plus grand est : ",Nbmax)
print("la position du nombre est : ",pos)

