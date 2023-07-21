# Write a Python function that takes a list of numbers as input and returns the sum of all the numbers in the list.
mylist1=[20,40,32,6,78,100]

# Using for loop with range
total=0
for i in range(len(mylist1)):
    total=total+mylist1[i]
print("SUM: ", total)
