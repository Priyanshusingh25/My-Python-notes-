# writing a program to store 6 fruits
# g1 = input("Enter fruit number 1")
# g2 = input("Enter fruit number 2")
# g3 = input("Enter fruit number 3")
# g4 = input("Enter fruit number 4")
# g5 = input("Enter fruit number 5")
# g6 = input("Enter fruit number 6")

# myFruitList = [g1, g2, g3, g4, g5, g6]
# print(myFruitList)

# write a program to accept marks of seven students and display them in a sorted manner

# s1 = int(input("marks of student 1 :"))
# s2 = int(input("marks of student 2 :"))
# s3 = int(input("marks of student 3 :"))
# s4 = int(input("marks of student 4 :"))
# s5 = int(input("marks of student 5 :"))
# s6 = int(input("marks of student 6 :"))
# s7 = int(input("marks of student 7 :"))

# mylist = [s1, s2, s3, s4, s5, s6, s7]
# mylist.sort()
# print(mylist)

# check that a tuple cannot be changed in a python

# a = (1, 3, 4, 6, 7, 8)
# a[3] = 6
# print(a)

# write a program to sum a list with 4 numbers

# a = [1, 2, 3, 4]
# print(a[0]+a[1]+a[2]+a[3])
# print(sum(a))

# write a program to count the number in the tuple

# a = (3, 5, 6, 7, 8, 0, 0, 0)
# print(a.count(0))

# create a dictionary of hindi words with values as their english translation provide user with an option to look it up


# user = input("Enter the hindi word?")
# print(user)
# createDict = {
#     "mahsoos": " to feel \n",
#     "soch": "to think"
# }

# print(createDict['mahsoos'], createDict['soch'])

# to input eight numbers from the user and display all the unique numbers

# user = input("Enter any number from the below eight number :")
# user = int()

# user = (1, 2, 3, 4, 6, 7, 8)
# print(user)

# 18 int and 18 string values
# a = {18, "18"}
# print(a)

# length of set 5 :

# a = set()
# a.add(20)
# a.add(20.0)
# a.add("20")
# print(len(a))
# print(type(a))
# print(a)

# multiplication table of a given number

# num = int(input("Enter the number"))   # goes from 1 to 10
# for i in range(1, 11):
#     print(f"{num}X {i}={num*i} ")  # f strings
#     print(str(num)+"X" + str(i) + "=" + str(i * num))

# greet all the persons name starting with a variable "a"


l1 = ["mariam", "shubham", "sabnaaj", "mukesh"]

for name in l1:
    if name.endswith("m"):  # we can use startswith also
        print(" have  a great year!" + name)
else:
    print("none")
