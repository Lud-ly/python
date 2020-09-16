#excercice4.2
h = 0
m = 0

h = int(input("entrez les heures"))
m = int(input("puis les minutes"))
print("il est",h,"heures et",m,"minutes")

if m == 60:
    m == 0
    h == h + 1
if h  == 24:
    h == 0
    print("dans une minute il sera",h,"heure",m+1,"minutes")    