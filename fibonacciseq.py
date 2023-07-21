# Write a Python function that generates the first n numbers of the Fibonacci sequence, where n is taken as input.
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
# starting from 0 and 1.
total = 0

number = int(input('Enter a number: '))

# add numbers until number is zero
while number != 0:
    total += number  # total = total + number

    # take integer input again
    number = int(input('Enter a number: '))

print('total =', total)

