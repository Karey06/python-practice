# define the function
def factorial(z):
    #Initialize
 x = 1
#Use a for loop, looping from 1 to z + 1
 for i in range(1, z+1):
  x = x * i
 return x
#Show result
print(factorial(7))


