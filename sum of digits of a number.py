def summation(number):
    total = 0
    for i in str(number):
        total = total + int(i)
    return total
print("Sum:" + str(summation(12583)))

