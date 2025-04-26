def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*factorial(num-1)
while True:
    try:
        num = int(input("Input num:"))
        if num <0:
            print("Invalid input")
        else:
            print(factorial(num))
            break
    except ValueError:
        print("Invalid input")
