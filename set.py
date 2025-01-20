thisset = {"apple", "banana", "cherry"}
print(thisset)

#no duplicates (1 and True are the same, false and 0 are also)
#no index access
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)



thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #discard() is also appropriate
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop() #remove random element
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)      #also union

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)  #set3=set1 & set2
print(set3)


