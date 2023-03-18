
# create an empty set

y = set()
print(type(y))

# adding values to an empty set

y.add(3)
y.add(6)
y.add(3 > 5)
y.add((4, 5, 6))  # only for tuples
print(y)

print(len(y))  # prints the length of the set

y.remove(3 > 5)  # removes the particular element
print(y)


print(y.pop())  # removes random values in the set
print(y)

print(y.clear())  # empties the set
