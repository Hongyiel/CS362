# Program 1
# File that contains the tests
# File that contains the code/implementation.

def FizzBuzz(number):
        if number % 3 == 0:
            if number % 15 == 0:
                return "FizzBuzz"
            else:
                return "Fizz"
        elif number % 5 == 0:
            if number % 15 == 0:
                return "FizzBuzz"
            else:
                return "Buzz"
        else:
            return number
# arr
array = []
for number in range(1,101):
    array.append(FizzBuzz(number))

print(array)
