#exercice7.4
"""
Tableau online_players()
Debut
online_players.remove
Ecrire "Rang de la valeur à supprimer ?"
ecrire "element suprimé"
Lire online_players
online_players[0] ← "99"
ecrire modifié
append ← "150"
extend ← element online_players
suprimer element online_players
clear online_players
Fin"""
online_players = ["1", "2", "3", "5","18"]
print("tableau initial",online_players)
online_players.pop(input("suprimmez un element"))
print("element suprimé",online_players)
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
