def fizzBuzz(n): #with conditions up to 65
    if (n % 3 == 0) and (n % 5 == 0):
        return "FizzBuzz"
    if (n % 3 == 0):
        return "Fizz"
    if (n % 5 == 0):
        return "Buzz"
    if (n % 6 == 0):
        return "Fizz"
    if (n % 9 == 0):
        return "Fizz"
    if (n % 10 == 0):
        return "Buzz"
    if (n % 12 == 0):
        return "Fizz"
    if (n % 15 == 0):
        return "FizzBuzz"
    if (n % 18 == 0):
        return "Fizz"
    if (n % 20 == 0):
        return "Buzz"
    if (n % 21 == 0):
        return "Fizz"
    if (n % 24 == 0):
        return "Fizz"
    if (n % 25 == 0):
        return "Buzz"
    if (n % 27 == 0):
        return "Fizz"
    if (n % 30 == 0):
        return "FizzBuzz"
    if (n % 33 == 0):
        return "Fizz"
    if (n % 35 == 0):
        return "Buzz"
    if (n % 36 == 0):
        return "Fizz"
    if (n % 39 == 0):
        return "Fizz"
    if (n % 40 == 0):
        return "Buzz"
    if (n % 42 == 0):
        return "Fizz"
    if (n % 45 == 0):
        return "FizzBuzz"
    if (n % 48 == 0):
        return "Fizz"
    if (n % 50 == 0):
        return "Buzz"
    if (n % 51 == 0):
        return "Fizz"
    if (n % 54 == 0):
        return "Fizz"
    if (n % 55 == 0):
        return "Buzz"
    if (n % 57 == 0):
        return "Fizz"
    if (n % 60 == 0):
        return "FizzBuzz"
    if (n % 63 == 0):
        return "Fizz"
    if (n % 65 == 0):
        return "Buzz"
    return n

for i in range(1, 66):
    print(fizzBuzz(i))
