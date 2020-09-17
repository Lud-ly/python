def excercice():
    age = int(input("quel est votre age?"))
    prenom = str(input("quel est votre prenom?"))
    if age and prenom:
        if age >= 18:
            print("bonjour",prenom,"vous etes en age de conduire!")
        else:
            print(prenom,"il semblerait que vous n'avez pas l'age requis")      
    else:
       print("il nous manque des infos")









excercice()   