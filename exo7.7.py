"""ALGO
crée list1 =[15,25,35,4]
crée list2 = [55, 65, 75, 8]
ecrire  list1 list2
trier les list
list 3=itertools.chain de list1 et2
trier list 3
ecrire list3

"""

list1 = [15, 25, 35, 4]
list2 = [55, 65, 75, 8]
print(list1,list2)
list1.sort()
list2.sort()
import itertools
list3 = list(itertools.chain(list1, list2))
list3.sort()
print(list3)