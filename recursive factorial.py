def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number*factorial(number-1)
while True:
    try:
        number = int(input("Input number:"))
        if number <0:
            print("Invalid input")
        else:
            print(factorial(number))
            break
    except ValueError:
        print("Invalid input")
