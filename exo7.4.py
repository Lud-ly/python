#exercice7.4
online_players=[]
    
for i in range(5):
    valeur = input("entrer des valeurs dans le tableau : ")
    online_players+=valeur
   

print("tableau initial",online_players)
online_players.pop(int(input("suprimmez un element par l'index : ")))
print("element suprimé",online_players)
"""
online_players[0] = "99"
print(" ajouter element",online_players)
online_players.append("150")
online_players.extend(["157", "32" , "14", "15" ,"27" , "77"])
print("ajouter des element",online_players)
print("nbr d'element total", len(online_players))
online_players.pop(3)
online_players.remove(input("suprimmez un element"))
print("element suprimé",online_players)
online_players.clear()
print("clear = tableau vidé", online_players)
"""