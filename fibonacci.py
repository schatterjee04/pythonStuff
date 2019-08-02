def fibonacci(nextPrevious, previous, count):
    current = previous + nextPrevious
    limit = count
    print(current)
    if limit > 3:
        fibonacci(previous, current, limit-1)
first = 0
second = 1
print("Welcome to the fibonacci number generator.")
counterLimit = 0;
try:
    counterLimit = int(input("How many values would you like?\n"))
except(TypeError, ValueError):
    print("Please enter a number!")
print(first)
print(second)
fibonacci(first, second, counterLimit)
