# Write a Python function that takes an integer as input and calculates its factorial.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input factiorial number : "))
print(factorial(n))
