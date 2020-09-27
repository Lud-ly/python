phrase = input("Entrez la phrase : ")
delete = int(input("Entrez le rang du caractère à supprimer : "))

phrase = phrase[:delete] + phrase[delete+1:]

print("la nouvelle phrase est :",phrase)
newPhrase = input("Entrez la phrase : ")
newPhrase = newPhrase.replace(phrase,newPhrase[delete-1])
print(newPhrase+phrase)
