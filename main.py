from linked_list import MyList, ListNode
from myclass import Cat

cat1=Cat("Blue", 3, "Vasya")
cat2=Cat("Red", 2, "Fedya")
cat3=Cat("White", 5, "Kolya")

lst=MyList()
lst.push(cat1)
lst.push(cat2)
lst.push(cat3)
print("Cats are added: ")
for i in lst:
   i.define()
print("Let's pop last added Cat: ")
lst.pop()
for i in lst:
   i.define()



