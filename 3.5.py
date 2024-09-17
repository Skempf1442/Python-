# create an empty list, says to the user to enter names 
names = []

#enter names in 
for i in range(5):
    name = input(f"Enter name {i+1}:")
    names.append(name)

#print names out 
print(f"\nOriginal list of names:")
print(names)

#bubble sort, alphabetically
names.sort()
print(names)

#print sorted names 
print("\n Sorted names list (ascending order):")
print(names)

#reverse order 
names.reverse()

#print list 
print("\nReversed list of names:")
print(names)