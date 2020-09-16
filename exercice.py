dico ={
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
#"print toutes les key du dictionnaire"
#"print toutes les values"
#boucler les values
print(dico.items())
print(dico.keys())
for x in dico.keys():
    print(x)
for x in dico.values():
    print(x)    
dico["color"] = "red"
dico["chevaux"] = "550cv"
for x,y in dico.items():
    print(x,y)
my_var = "{s} toto"
print(my_var.format(s="my name is"))
print(len(dico))