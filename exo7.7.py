list1=[]
list2=[]
for i in range(5):
   valList1 = input("entrer des valeurs dans le tableau1 : ")
   valList2 = input("entrer des valeurs dans le tableau2 : ")
   list1+=valList1
   list2+=valList2

print(list1,list2)
list1.sort()
list2.sort()
import itertools
list3 = list(itertools.chain(list1, list2))
list3.sort()
print(list3)