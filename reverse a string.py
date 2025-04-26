# defining the function
def reverse_string(string):
    reversed_str=""
    #The loop goes through the characters from the end index to the start index
    for i in range (len(string)-1,-1,-1):
        reversed_str+=string[i]
    return reversed_str
print(reverse_string("Karanja"))
